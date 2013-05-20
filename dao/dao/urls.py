from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('frontend.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('articles.urls')),
    url(r'^markitup/', include('markitup.urls'))
)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += staticfiles_urlpatterns()