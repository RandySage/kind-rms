from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^browserid/', include('django_browserid.urls')),
    url(r'^spec/', include('kind.urls', namespace='kind')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('kind.urls', namespace='kind')),
)
