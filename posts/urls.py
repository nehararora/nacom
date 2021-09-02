from django.conf.urls import url

from . import views
from .models import Post

urlpatterns = [
    # category views

    # /home - same as /category/home/1
    url(r'^$', views.category_view, name='home_view'),

    # /<name> - same as /category/<name>/1
    url(r'^category/(?P<category_name>\w+)/$', views.category_view, name='home_view'),

    # /category/<name>/<page_number>
    url(r'^category/(?P<category_name>\w+)/(?P<page_num>[0-9]+)/$',
        views.category_view, name='category_view'),

    # tag views

    # /tag/<name> - same as /tag/<name>/1
    url(r'^tag/(?P<tag_name>\w+)/$', views.tag_view, name='tag_view'),

    # /tag/<name>/<page_number>
    url(r'^tag/(?P<tag_name>\w+)/(?P<page_num>[0-9]+)/$', views.tag_view, name='tag_view'),

    # permalink
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<post_url>[0-9A-Za-z-]+)$',
        views.PostDetailView.as_view(model=Post, date_field="post_datetime"), name='post_detail'),
]
