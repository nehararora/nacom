"""
Utility methods for data access.
"""
from posts.models import Post
from posts.models import Tag
from posts.models import Category
from django.shortcuts import get_object_or_404

###############################
def get_recent_posts(num=5):
  """
  get n most recent posts ordered by post time.
  """
  return Post.objects.all().order_by(u'-post_datetime')[0:num]

###############################
def get_all_posts():
  """
  get all Post objects ordered by post time.
  """
  return Post.objects.all().order_by(u'-post_datetime')

###############################
def get_posts_by_tags(tags):
  """
  get Post objects with any tag from list tags. 
  If an object has more than one tag from list, 
  the returned list will only have one instance.
  """
# TODO: look at http://groups.google.com/group/django-users/browse_thread/thread/065ad54287e10bbd/8f410e522e003a9a for getting posts that match ALL the tags in the list.

  # need distinct here since same post might be tagged by mutiple
  # tags from tag_list
  return Post.objects.filter(post_tags__tag_name__in=tags) \
                .order_by(u'-post_datetime').distinct()

###############################
def get_tag(tag_name):
  """
  get Tag object.
  """
  return get_object_or_404(Tag, tag_name=tag_name)

###############################
def get_category(category_name):
  """
  get Category object.
  """
  return get_object_or_404(Category, category_name=category_name)

###############################
def get_all_categories():
  """
  get all categories. orderd by name.
  """
  return Category.objects.order_by(u'category_name')

###############################
def get_all_tags():
  """
  get all tags. ordered by name.
  """
  return Tag.objects.order_by(u'tag_name')

###############################
def get_tags_by_category(categoryname):
  """
  get Tag objects that belong to Category 'categoryname'
  """
  return Tag.objects.filter(category__category_name=categoryname)

###############################
def get_post_by_slug(post_slug):
  """
  get Post objects with slug matching input. In
  case the slug is not uniqe multiple objects
  are returned. ordered by post time.
  """
  return Post.objects.all().filter(post_url__exact=post_slug) \
                    .order_by(u'-post_datetime')

###############################
