# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
                ('category_description', models.TextField()),
                ('category_heading', models.TextField(blank=True)),
                ('category_content_header', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_author', models.CharField(max_length=128)),
                ('post_datetime', models.DateTimeField(auto_now_add=True)),
                ('post_heading', models.CharField(blank=True, max_length=1024)),
                ('post_content', models.TextField()),
                ('post_content_author', models.CharField(blank=True, max_length=1024)),
                ('post_comments', models.TextField(blank=True)),
                ('post_mime_type', models.CharField(blank=True, max_length=256)),
                ('post_url', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255, unique=True)),
                ('tag_description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_tags',
            field=models.ManyToManyField(to='posts.Tag'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_tags',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Tag'),
        ),
    ]
