from __future__ import unicode_literals
from django.db import models


"""
Model class for the posts app.
"""


class Tag(models.Model):
    tag_name = models.CharField(max_length=256, unique=True)
    tag_description = models.TextField()


class Category(models.Model):
    category_name = models.CharField(max_length=256, unique=True)
    category_tags = models.ManyToManyField(Tag, blank=True, null=True)
    category_description = models.TextField()
    category_content_header = models.TextField(blank=True)


class Post(models.Model):
    post_author = models.CharField(max_length=128)
    post_datetime = models.DateTimeField(editable=False)
    post_heading = models.CharField(max_length=1024, blank=True)
    post_content = models.TextField()
    post_content_author = models.CharField(max_length=1024, blank=True)
    post_tags = models.ManyToManyField(Tag)
    post_comments = models.TextField(blank=True)
    post_mime_type = models.CharField(max_length=256, blank=True) # TODO: remove??
    post_url = models.SlugField()

