# Generated by Django 5.0.2 on 2024-04-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Learning", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="product",
            name="summary",
            field=models.TextField(null=True),
        ),
    ]