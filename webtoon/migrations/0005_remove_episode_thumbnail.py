# Generated by Django 4.2.7 on 2024-01-11 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0004_webtoon_uploaddays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='thumbnail',
        ),
    ]
