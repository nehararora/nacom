"""
views for the posts app.
"""
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.core.paginator import EmptyPage, PageNotAnInteger
# from django.views.generic import DetailView
from django.views.generic import DateDetailView

from . import pagination
from . import postutil
from .models import Post

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# TODO: convert everything to generic class based views?

def category_view(request, category_name="home", page_num=1):
    """
    View to display posts by Category.

    :param request: The HTTP request
    :param category_name: The category to use for pulling posts.
    :param page_num: Page number
    :return: http response
    """
    template = get_template('posts/post_list_template.html')

    categories = postutil.get_all_categories()
    all_tags = postutil.get_all_tags()

    # category tags to pass on to the template for highlighting.
    tags = [t.tag_name for t in postutil.get_tags_by_category(category_name)]

    requested_category = postutil.get_category(category_name=category_name)

    # un-paginated posts
    all_posts = postutil.get_posts_by_tags(tags)

    # get our custom paginator
    paginator = pagination.Pages(all_posts, 5)

    # TODO: need to fix last empty page - only happens in dev?
    try:
        posts = paginator.page(page_num)

    except EmptyPage:
        # on out of range return last page
        raise Http404("Page does not exist")

    # create context to pass into the template.
    context = {
        'content_header': requested_category.category_name,
        'categories': categories,
        'requested_category': requested_category,
        'requested_tags': tags,
        'all_tags': all_tags,
        'posts': posts,
        'view_name': 'category_view',
        'path': requested_category,
    }

    return HttpResponse(template.render(context, request))


def tag_view(request, tag_name, page_num=1):
    """
    View to display all posts tagged with tag_name.

    :param request: The HTTP request
    :param tag_name: Requested tag name
    :param page_num: Page number
    :return: Http Response
    """
    template = get_template('posts/post_list_template.html')
    categories = postutil.get_all_categories()
    all_tags = postutil.get_all_tags()
    tags = (tag_name,)
    all_posts = postutil.get_posts_by_tags(tags)

    paginator = pagination.Pages(all_posts, 5)

    try:
        posts = paginator.page(page_num)

    except EmptyPage:
        # on out of range return last page
        logger.warn("Empty page.")
        raise Http404("Page does not exist")

    context = {
        'content_header': tag_name,
        'categories': categories,
        'requested_tags': tags,
        'all_tags': all_tags,
        'posts': posts,
        'view_name': 'tag_view',
        'path': tag_name,
    }

    return HttpResponse(template.render(context, request))


class PostDetailView(DateDetailView):
    """
    Single Post View.

    Displays posts matching slug and date from the url. In case of multiple
    slug matches, displays posts ordered by date.
    """
    model = Post
    slug_field = "post_url"
    slug_url_kwarg = "post_url"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        """
        hook for overriding context
        :param kwargs:
        :return:
        """
        context = super(DateDetailView, self).get_context_data(**kwargs)

        # setup extra context
        context['categories'] = postutil.get_all_categories()
        context['all_tags'] = postutil.get_all_tags()
        context['view_name'] = 'post_detail'
        print(context)

        return context
