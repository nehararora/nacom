"""
views for the posts app.
"""
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.core.paginator import EmptyPage, PageNotAnInteger
from . import pagination
from . import postutil
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


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
    logger.debug("Tags: ".format(tags))
    # logger.debug("categories: {0}".format(categories))
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

    print("Context: {0}".format(context))

    return HttpResponse(template.render(context, request))


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

