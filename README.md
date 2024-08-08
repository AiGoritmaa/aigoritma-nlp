# Nasıl Çalıştırlır ve İndirilir?

```bash
  git clone https://github.com/AiGoritmaa/aigoritma-nlp
```
projenin indirilmesi
```bash
  cd aigoritma-nlp
```
projenin olduğu dizine gidilmesi
```bash
  pip install -r requirement.txt
```
gerekli kütüphanelerin indirimesi
```bash
  python manage.py runserver
```
projenin çalıştırılması
```bash
  http://127.0.0.1:8000/
```
bu url ile siteye giriş yapabilirsiniz

 # Kullanılan Veri Seti
 -nltk kütüphanesinin stopwords ve açık kaynak olarak kullandığımız argo kelimeleri barındıran veri setlerini kullanmaktayız. 
 
 -stopwords veri seti nltk kütüphanenin yükselenmesiyle kendi içinde bulunmaktadır. Bu veri seti kendi içinde türkçe durak kelimelerini bulundurmaktadır.
 
 -Argo kelimelerin olduğu veri setimiz ise projenin ana dizinde json dosyası olarak bulunmaktadır.
 
 -argo kelimeler veri setinin kaynağı: https://github.com/ooguz/turkce-kufur-karaliste
