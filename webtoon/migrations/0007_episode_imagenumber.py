# Generated by Django 4.2.7 on 2024-02-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0006_episode_thumbnail_alter_webtoon_titleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='imageNumber',
            field=models.IntegerField(default=0),
        ),
    ]
