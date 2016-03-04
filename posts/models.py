from __future__ import unicode_literals
from django.db import models

"""
Model class for the posts app.
"""


class Tag(models.Model):
    tag_name = models.CharField(max_length=255, unique=True)
    tag_description = models.TextField()

    def __str__(self):
        return self.tag_name


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    category_tags = models.ManyToManyField(Tag, blank=True, null=True)
    category_description = models.TextField()
    category_heading = models.TextField(blank=True)
    category_content_header = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_author = models.CharField(max_length=128)
    post_datetime = models.DateTimeField(auto_now_add=True)
    post_heading = models.CharField(max_length=1024, blank=True)
    post_content = models.TextField()
    post_content_author = models.CharField(max_length=1024, blank=True)
    post_tags = models.ManyToManyField(Tag)
    post_comments = models.TextField(blank=True)
    post_mime_type = models.CharField(max_length=256, blank=True)
    post_url = models.SlugField()

    def __str__(self):
        return self.post_url
