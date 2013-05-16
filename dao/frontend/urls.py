from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

# pylint: disable=C0103
urlpatterns = patterns(
    'frontend.views',
    url(r'^$', views.index, name='index'),
    url(r'^example-page$', views.page, name='example-page')
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
