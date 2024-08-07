from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from app.models import Category, Comment, News, Visitor
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.classify import NaiveBayesClassifier
from collections import defaultdict
import string
from collections import Counter
import random
import re

# Create your views here.
def index(request):
    select_news = ""
    news = News.objects.all()
    categories = Category.objects.all()
    visitor = Visitor.objects.get(session_key=request.session.session_key)  
    paginator = Paginator(news, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if(visitor.visited_categories["categories"]):
        if(len(visitor.visited_categories["categories"])==10):
            selected_category = en_cok_tercih_edilen_kategori(visitor.visited_categories["categories"])
            visitor.visited_categories["categories"] = []
            visitor.visited_categories["categories"].append(selected_category)
            visitor.save()
        selected_category = en_cok_tercih_edilen_kategori(visitor.visited_categories["categories"])
        select_news = News.objects.filter(category_id=selected_category)[:2]
    return render(request, 'app/index.html', {'page_obj': page_obj, "selected_news":select_news, "categories":categories})

def categories(request):
    categories = Category.objects.all()
    return render(request, "app/categories.html", {"categories":categories})

def news_details(request, slug):
    visitor = Visitor.objects.get(session_key=request.session.session_key)
    news = News.objects.get(slug=slug)
    comments = news.comments.all()
    visitor.visited_categories["categories"].append(news.category.id)
    visitor.save()
    return render(request, "app/news_details.html", {"new":news, "comments":comments})

def news_content_summary(request, slug):
    nltk.download('punkt')
    nltk.download('stopwords')
    news = News.objects.get(slug=slug)
    summary_content = ""
    try:
        summary_content = summarize(news.content)
    except:
        print("hata")
    
    return render(request, "app/news_details.html", {"new":news, "summary_content":summary_content})

def news_filter_category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    news = category.newss.all()
    selected_category = category.id
    paginator = Paginator(news, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "app/category_news.html", { "categories":categories, "selected_category":selected_category, "page_obj":page_obj})

def add_comment(request):
    if request.method == "POST":
        visitor = Visitor.objects.get(session_key=request.session.session_key)
        news = News.objects.get(slug=request.POST["news_slug"])
        comment = Comment.objects.create(username=request.POST["username"], content=request.POST["content"],news=news,visitor=visitor)
        comment.save()
        return HttpResponseRedirect("/news/" + request.POST["news_slug"])

def summarize(text, n=3):
    # Metni cümlelere bölme
    sentences = sent_tokenize(text)

    # Kelimeleri küçük harfe çevirme, durak kelimeleri ve noktalama işaretlerini kaldırma
    stop_words = set(stopwords.words('turkish'))
    word_frequencies = defaultdict(int)

    for word in word_tokenize(text.lower()):
        if word not in stop_words and word not in string.punctuation:
            word_frequencies[word] += 1

    # Kelime frekanslarını normalize etme
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / max_frequency

    # Cümle puanlama
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word]

    # En yüksek puanlı cümleleri seçme
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
    summary = ' '.join(summarized_sentences)
    return summary

def en_cok_tercih_edilen_kategori(etkinlikler):
    if not etkinlikler:
        return None
    
    kategori_sayaci = Counter(etkinlikler)
    en_cok_tercih_edilen = kategori_sayaci.most_common(1)
    
    return en_cok_tercih_edilen[0][0] if en_cok_tercih_edilen else None