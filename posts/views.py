"""
views for the posts app.
"""
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import postutil
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def category_view(request, category_name="home", page_num=1):
    """
    View to display posts by Category.

    :param request: the HTTP request
    :param category_name: The category to use for pulling posts.
    :param page_num: Page number
    :return: http response
    """
    template = get_template('posts/post_list_template.html')

    categories = postutil.get_all_categories()
    requested_category = postutil.get_category(category_name=category_name)
    tags = postutil.get_tags_by_category(category_name)

    all_tags = postutil.get_all_tags()

    # TODO: posts = postutil.get_posts_by_tags(tags)
    all_posts = postutil.get_all_posts()
    paginator = Paginator(all_posts, 5)
    logger.warning("Page Number is " + str(page_num))
    try:
        posts = paginator.page(page_num)
    except EmptyPage:
        # on out of range return last page
        raise Http404("Page does not exist")
        # posts = paginator.page(paginator.num_pages-1)

    # posts = postutil.get_posts_by_tags(tags)
    logger.warning("posts: {0}".format(posts))
    logger.warning("Categories: {0}".format(list(categories)))
    logger.warning("Requested: {0}".format(requested_category))
    logger.warning("Tags: {0}".format(tags))

    context = {
        'content_header': requested_category.category_name,
        'categories': categories,
        'requested_category': requested_category,
        'tags': [t.tag_name for t in tags],
        'all_tags': all_tags,
        'posts': posts,
    }

    return HttpResponse(template.render(context, request))


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


# there is no date archive setup as of 2009-04-04, so the only
# way this view gets called right now is if someone puts in the
# date url in the address bar *or* if some post does not have
# the post_url field populated, in which case the post url link
# goes through the date view.
def date_view(request):
    """
    Display posts by date.

    wrapper view that sets up the extra_context before calling django's generic date views.

    :param request:
    :param year:
    :param mode:
    :param month:
    :param day:
    :return:
    """
    return HttpResponse("Hello date view world")


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

