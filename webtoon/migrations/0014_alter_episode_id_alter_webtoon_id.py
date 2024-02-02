# Generated by Django 4.2.7 on 2024-02-02 13:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0013_alter_episode_thumbnail_alter_webtoon_titleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='webtoon',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
