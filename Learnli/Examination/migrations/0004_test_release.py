# Generated by Django 5.1.1 on 2024-12-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examination', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='release',
            field=models.BooleanField(default=False),
        ),
    ]