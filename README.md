# Proje Hakkında
Bu proje Teknofest TDDİ yarışması serbest kategori metin özetleme konusu için yapılmışıtr

Proje Django tabanlı web uygulaması olup Doğal Dil İşleme teknikleri ve metin özetleme algoritması ile haber içeriklerinin özetlenmesini yapmaktadır.


# Nasıl İndirilir ve Çalıştırlır?

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
 - Projede nltk kütüphanesinin stopwords veri seti kullanılmıştır. 
 
 - stopwords veri seti nltk kütüphanenin yükselenmesiyle kendi içinde bulunmaktadır. Bu veri seti kendi içinde türkçe durak kelimelerini bulundurmaktadır.

- uygulama içinde nltk.download("stopwrods") kodu ile veri seti yüklenmektedir.
 # Ek Olarak
- Projenin içinde olan haber içerikleri haber.com sitesinden güncel haberler olarak alınmıştır.
