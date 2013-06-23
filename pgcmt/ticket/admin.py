from django.db import models
from django.contrib import admin
from ticket.models import Ticket,Project,RequestUser

class TicketAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_display = ('project','user','content','created_at')
    list_filter = ['created_at']


class ProjectAdmin(admin.ModelAdmin):
    search_fields = [ "name" ]
    fields = ('name', 'description','created_at')
    list_display = ('name', 'description', 'created_at')

class RequestUserAdmin(admin.ModelAdmin):
    search_fields = [ "username" ]
    list_display = [ "username","created_at" ]

admin.site.register(Ticket,TicketAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(RequestUser,RequestUserAdmin)
