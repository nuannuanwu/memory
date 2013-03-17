# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("memory.views.frontend",
     url(r'^$', "index", name='home'),
     url('^index_test/$', "index_test", name="index_test"),
     url('^index_test/undefined/$', "index_test", name="index_test"),
     url('^test/$', "test_index", name="test"),
     url('^testone/$', "test_one", name="test1"),
     url('^testone1/$', "test_one_extra", name="test1_extra"),
     url('^testtwo/$', "test_two", name="test2"),
     url('^test3/$', "test3", name="test3"),
     
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/',include('grappelli.urls')), 
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()