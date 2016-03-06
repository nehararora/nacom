from django.conf.urls import url

from . import views

urlpatterns = [
    # category views

    # /home - same as /category/home/1
    url(r'^$', views.category_view, name='home_view'),

    # /<name> - same as /category/<name>/1
    url(r'^category/(?P<category_name>\w+)/$', views.category_view, name='home_view'),

    # /category/<name>/<page_number>
    url(r'^category/(?P<category_name>\w+)/(?P<page_num>[0-9]+)$',
        views.category_view, name='category_view'),

    # tag views

    # /tag/<name> - same as /tag/<name>/1
    url(r'^tag/(?P<tag_name>\w+)/$', views.tag_view, name='tag_view'),

    # /tag/<name>/<page_number>
    url(r'^tag/(?P<tag_name>\w+)/(?P<pagenum>[0-9]+)/$', views.tag_view, name='tag_view'),

    # date views
    url(r'^date/$', views.date_view),

    # slug views
    url(r'^slug/$', views.slug_view),

    # about view
    url(r'^about/$', views.about_view, name='about')
]
