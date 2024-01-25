# Generated by Django 4.2.7 on 2024-01-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0007_alter_userprofile_introduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='introduction',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
