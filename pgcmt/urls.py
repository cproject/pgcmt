from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import DetailView, ListView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pgcmt.ticket.views.home', name='home'),
    # url(r'^pgcmt/', include('pgcmt.foo.urls')),
    url(r'^ticket/$','pgcmt.ticket.views.home',name='Home'),
    url(r'^ticket/create/project/$','pgcmt.ticket.views.createProject',name='CreateProject'),
    url(r'^ticket/create/ticket/$','pgcmt.ticket.views.createTicket',name='CreateTicket'),
    url(r'^ticket/projects/$','pgcmt.ticket.views.listProjects',name='Projects'),
    url(r'^ticket/project/(?P<project_name>\w+)/$','pgcmt.ticket.views.showProject',name='showProject'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
