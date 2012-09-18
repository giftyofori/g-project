from django.conf.urls import patterns, include, url
from django.conf import settings
import dj_simple_sms
import smart_report
import the_test

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RS_project.views.home', name='home'),
    # url(r'^RS_project/', include('RS_project.foo.urls')),
    url(r'^srport/', include('smart_report.urls'))

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root' : settings.STATIC_ROOT,
    }),
    
    url(r'^sms/',include(dj_simple_sms.urls))
)
