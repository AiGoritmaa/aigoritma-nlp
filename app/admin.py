from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Category, Comment, News, Visitor

# Register your models here.
admin.site.register(Visitor)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Comment)