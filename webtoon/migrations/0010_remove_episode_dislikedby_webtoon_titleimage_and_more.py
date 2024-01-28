# Generated by Django 4.2.7 on 2024-01-28 14:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0009_rename_rating_episode_totalrating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='dislikedBy',
        ),
        migrations.AddField(
            model_name='webtoon',
            name='titleImage',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
