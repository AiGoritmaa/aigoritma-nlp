# Generated by Django 5.0.7 on 2024-08-04 10:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_news_alt_content_alter_news_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="summary_content",
        ),
    ]
