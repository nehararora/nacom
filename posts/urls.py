from django.conf.urls import url

from . import views

urlpatterns = [
    # category views
    url(r'^$', views.category_view),

    # tag views
    url(r'^tag/$', views.tag_view),

    # date views
    url(r'^date/$', views.date_view),

    # slug views
    url(r'^slug/$', views.slug_view),

    # about view
    url(r'^about/$', views.about_view, name='about')
]
