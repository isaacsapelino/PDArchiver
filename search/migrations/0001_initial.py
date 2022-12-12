<<<<<<< HEAD
# Generated by Django 4.1.1 on 2022-12-12 07:12
=======
# Generated by Django 4.1.2 on 2022-12-12 07:12
>>>>>>> e7129e03aedc00b94f682ef4b83692242995b247

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import search.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('abstract', models.TextField()),
                ('year', models.DateField(default=datetime.date.today)),
                ('slug', models.SlugField(null=True)),
                ('document', models.FileField(upload_to=search.models.Thesis.user_directory_path)),
                ('authors', models.ManyToManyField(related_name='Authors', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Uploader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
