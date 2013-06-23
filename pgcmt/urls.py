from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import DetailView, ListView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ticket.views.home', name='home'),
    # url(r'^pgcmt/', include('foo.urls')),
    url(r'^ticket/$','ticket.views.home',name='Home'),
    url(r'^create/project/$','ticket.views.createProject',name='CreateProject'),
    url(r'^create/ticket/$','ticket.views.createTicket',name='CreateTicket'),
    url(r'^create/requestUser/$','ticket.views.createRequestUser',name='CreateRequestUser'),
    url(r'^projects/$','ticket.views.listProjects',name='Projects'),
    url(r'^search/$','ticket.views.searchTicket',name='searchTicket'),
    url(r'^project/(?P<project_name>\w+)/$','ticket.views.showProject',name='showProject'),
    url(r'^user/(?P<username>\w+)/$','ticket.views.showUser',name='showUser'),
    url(r'^requestuser/(?P<requestuser_id>\w+)/$','ticket.views.showRequestUser',name='showRequestUser'),
    url(r'^login/$','auth.views.check_login',name='Login'),
    url(r'^logout/$','auth.views.logout_view',name='Logout'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


#    url(r'^ticket/$','ticket.views.home',name='Home'),
#    url(r'^ticket/create/project/$','ticket.views.createProject',name='CreateProject'),
#    url(r'^ticket/create/ticket/$','ticket.views.createTicket',name='CreateTicket'),
#    url(r'^ticket/projects/$','ticket.views.listProjects',name='Projects'),
#    url(r'^ticket/search/$','ticket.views.searchTicket',name='searchTicket'),
#    url(r'^ticket/project/(?P<project_name>\w+)/$','ticket.views.showProject',name='showProject'),
#    url(r'^ticket/user/(?P<username>\w+)/$','ticket.views.showUser',name='showUser'),
#    url(r'^ticket/requestuser/(?P<requestuser_id>\w+)/$','ticket.views.showRequestUser',name='showRequestUser'),
#    url(r'^ticket/login/$','auth.views.check_login',name='Login'),
#    url(r'^ticket/logout/$','auth.views.logout_view',name='Logout'),