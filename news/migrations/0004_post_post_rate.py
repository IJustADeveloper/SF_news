# Generated by Django 4.1.3 on 2022-11-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_rate',
            field=models.IntegerField(default=0),
        ),
    ]
