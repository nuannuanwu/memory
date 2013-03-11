# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("memory.views.frontend",
     url(r'^$', "index", name='home'),
     url('^index/$', "index", name="home"),
     url('^test/$', "test_index", name="test"),
     
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/',include('grappelli.urls')), 
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )