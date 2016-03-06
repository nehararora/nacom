from django.conf.urls import url

from . import views

urlpatterns = [
    # category views

    # /home - same as /category/home/1
    url(r'^$', views.category_view, name='home_view'),

    # /<name> - same as /category/<name>/1
    url(r'^category/(?P<category_name>\w+)/$', views.category_view, name='home_view'),

    # /category/<name>/<page_number>
    url(r'^category/(?P<category_name>\w+)/$', views.category_view, name='category_view'),

    # tag views
    url(r'^tag/$', views.tag_view),

    # date views
    url(r'^date/$', views.date_view),

    # slug views
    url(r'^slug/$', views.slug_view),

    # about view
    url(r'^about/$', views.about_view, name='about')
]
