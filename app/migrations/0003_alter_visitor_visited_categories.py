# Generated by Django 5.0.7 on 2024-08-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_visitor_visited_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visitor",
            name="visited_categories",
            field=models.JSONField(),
        ),
    ]
