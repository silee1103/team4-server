# Generated by Django 4.2.7 on 2024-01-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0003_alter_comment_createdby_alter_comment_dislikedby_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webtoon',
            name='uploadDays',
            field=models.ManyToManyField(related_name='webtoons', to='webtoon.dayofweek'),
        ),
    ]
