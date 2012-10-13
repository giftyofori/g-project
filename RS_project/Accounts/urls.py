from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^logout/$', 'Accounts.views.logout'),
    url(r'^login/$', 'Accounts.views.login'), 
    url(r'^register/$', 'Accounts.views.register'),
    url(r'^/?next=/$', 'Accounts.views.login'), 
    
)