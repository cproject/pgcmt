from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import DetailView, ListView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ticket.views.home', name='Home'),

    url(r'^account/$','auth.views.changePassword',name='ChangePassword'),

    url(r'^show/project/(?P<project_name>\w+)/$','ticket.views.showProject',name='ShowProject'),
    url(r'^show/ticket/(?P<ticketId>\w+)$','ticket.views.showTicket',name='ShowTicket'),
    url(r'^show/user/(?P<username>\w+)/$','ticket.views.showUser',name='ShowUser'),
    url(r'^show/requestuser/(?P<requestuser_id>\w+)/$','ticket.views.showRequestUser',name='ShowRequestUser'),
    
    url(r'^create/project/$','ticket.views.createProject',name='CreateProject'),
    url(r'^create/ticket/$','ticket.views.createTicket',name='CreateTicket'),
    url(r'^create/requestUser/$','ticket.views.createRequestUser',name='CreateRequestUser'),

    url(r'^edit/ticket/(?P<ticketId>\w+)/$','ticket.views.editTicket',name='EditTicket'),
    url(r'^delete/ticket/$','ticket.views.deleteTicket',name='DeleteTicket'),

    url(r'^projects/$','ticket.views.listProjects',name='ListProjects'),
    url(r'^search/$','ticket.views.searchTicket',name='searchTicket'),

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