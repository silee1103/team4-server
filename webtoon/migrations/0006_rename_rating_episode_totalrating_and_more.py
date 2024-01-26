# Generated by Django 4.2.7 on 2024-01-26 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webtoon', '0005_alter_dayofweek_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='rating',
            new_name='totalRating',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='likedBy',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='ratedBy',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
                ('ratingOn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='webtoon.episode')),
            ],
            options={
                'unique_together': {('createdBy', 'ratingOn')},
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLike', models.BooleanField()),
                ('isDislike', models.BooleanField()),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('createdBy', 'content_type', 'object_id')},
            },
        ),
    ]
