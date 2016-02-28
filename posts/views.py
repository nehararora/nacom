from django.shortcuts import render

# Create your views here.
"""
views for the posts app.
"""
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
# from django.views.generic.dates import archive_day
# from django.views.generic.dates import archive_month
# from django.views.generic.dates import archive_year
# from django.views.generic.dates import object_detail

from posts.postutil import get_all_tags
from posts.postutil import get_all_categories
from posts.postutil import get_all_posts
from posts.postutil import get_posts_by_tags
from posts.postutil import get_tags_by_category
from posts.postutil import get_category
from posts.postutil import get_tag


###############################

# TODO: fix to use category.type=external
# (for apps)/home(for home page)
def category_view(request):
    """
    View to display posts by Category.

    :param request:
    :param category_name:
    :param mode:
    :param pagenum:
    :return:
    """
    return HttpResponse("Hello category world!")


###############################

def tag_view(request):
    """
    View to display all posts tagged with tag_name.

    :param request:
    :param tag_name:
    :param mode:
    :param pagenum:
    :return:
    """
    return HttpResponse("Hello tag view world")


###############################

# wrapper view that sets up the extra_context before
# calling django's generic date views.

# there is no date archive setup as of 2009-04-04, so the only
# way this view gets called right now is if someone puts in the
# date url in the address bar *or* if some post does not have
# the post_url field populated, in which case the post url link
# goes through the date view.
def date_view(request):
    """
    View to display posts by date.

    :param request:
    :param year:
    :param mode:
    :param month:
    :param day:
    :return:
    """
    return HttpResponse("Hello date view world")


###############################

def slug_view(request):
    """
    View to display post by slug and date.

    :param request:
    :param mode:
    :param year:
    :param month:
    :param day:
    :param slug:
    :return:
    """

    return HttpResponse("Hello Slug view world")


###############################

def about_view(request):
    """

    View for the about section. Grabs posts tagged with tag_name and pushes
    them to the about template. *Don't* add tag_name tag to the 'home'
    category if you don't want it to show up in the all posts section.
    Should merge this with the category view - can be handled using the
    'about' category, which only has the 'meta' tag.
    only using this to keep the urls separated.

    :param request:
    :param mode:
    :param tag_name:
    :param pagenum:
    :return:
    """
    return HttpResponse("Hello about view world")


###############################
