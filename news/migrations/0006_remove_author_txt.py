# Generated by Django 4.1.3 on 2022-11-24 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_author_txt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='txt',
        ),
    ]