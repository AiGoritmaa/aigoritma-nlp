from django.db import models
from django.utils.text import slugify

class Visitor(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    visited_categories = models.JSONField(default={"categories":[]},blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.session_key} visited {self.path} at {self.timestamp}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, default="", null=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, kwargs)
    

class News(models.Model):
    title = models.CharField(max_length=255)
    alt_content = models.TextField(null=True)
    content = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='newss')
    slug = models.SlugField(default="", null=False, blank=True)

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super().save(args, kargs)
    
    def __str__(self) -> str:
        return f"{self.category}"
    
class Comment(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name="comments")
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    username = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    