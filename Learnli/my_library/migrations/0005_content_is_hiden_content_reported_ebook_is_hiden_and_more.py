# Generated by Django 5.1.1 on 2024-12-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_library', '0004_content_language_content_paid_users_content_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='is_hiden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='content',
            name='reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ebook',
            name='is_hiden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ebook',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]