# Generated by Django 5.0.7 on 2024-08-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_news_summary_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
