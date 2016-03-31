"""
Utility methods for data access.
"""
from posts.models import Post
from posts.models import Tag
from posts.models import Category
from django.http import Http404
from django.shortcuts import get_object_or_404

# TODO: Add caching layer.


def get_recent_posts(num=5):
    """
    Get n most recent posts ordered by post time.

    :param num:
    :return:
    """

    return Post.objects.all().order_by('-post_datetime')[0:num]


def get_all_posts():
    """
    Get all Post objects ordered by post time.
    """
    return Post.objects.all().order_by('-post_datetime')


def get_posts_by_tags(tags):
    """
    Get Post objects with any tag from list tags. If an object has more than
    one tag from list, the returned list will only have one instance.

    :param tags: Tags
    :return:
    """

    # need distinct here since same post might be tagged by multiple from tag_list

    posts = Post.objects.filter(post_tags__tag_name__in=tags).order_by('-post_datetime').distinct()
    if not posts:
        raise Http404('Page does not exist')

    return posts


def get_tag(tag_name):
    """
    Get Tag object.

    :param tag_name:
    :return:
    """
    return get_object_or_404(Tag, tag_name=tag_name)


def get_category(category_name):
    """
    Get Category object.

    :param category_name:
    :return:
    """
    return get_object_or_404(Category, category_name=category_name)


def get_all_categories():
    """
    Get all categories ordered by name.
    """
    return Category.objects.order_by('category_name')


def get_all_tags():
    """
    Get all tags ordered by name.
    """
    return Tag.objects.order_by('tag_name')


def get_tags_by_category(category_name):
    """
    Get Tag objects that belong to Category 'category_name'

    :param category_name:
    :return:
    """
    return Tag.objects.filter(category__category_name=category_name)


# TODO: not being used - remove?
def get_post_by_slug_and_date(post_slug):
    """
    Get Post objects with slug matching input. In case the slug is not unique
    multiple objects ordered by post time are returned.

    :param post_slug:
    :return:
    """
    return Post.objects.all().filter(post_url__exact=post_slug).order_by(u'-post_datetime')
