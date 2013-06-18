from django.db import models
from django.contrib import admin
from pgcmt.ticket.models import Ticket,Project

class TicketAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_display = ('project_id','user_id','content','created_at')
    list_filter = ['created_at']


class ProjectAdmin(admin.ModelAdmin):
    search_fields = [ "name" ]
    fields = ('name', 'created_at')
    list_display = ('name', 'created_at')

admin.site.register(Ticket,TicketAdmin)
admin.site.register(Project,ProjectAdmin)
