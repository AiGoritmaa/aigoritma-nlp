from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("categories", views.categories, name='categories'),
    path("news/<slug:slug>",views.news_details,name="news_details"),
    path("news/summary/<slug:slug>",views.news_content_summary),
    path("news/category/<slug:slug>", views.news_filter_category),
    path("news/comment/add", views.add_comment)
]
