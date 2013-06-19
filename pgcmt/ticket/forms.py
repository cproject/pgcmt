# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from pgcmt.ticket.views import Project,RequestUser
#from cover.models import Cover

class CreateProjectForm(forms.Form):
    """
        Upload a new Cover Form
    """
    name = forms.CharField(label=u"Project")
    #created_at = forms.DateTimeField(label=u"Date")
class CreateTicketForm(forms.Form):
    project_id = forms.ModelChoiceField(label=u"Project",queryset=Project.objects.all())
    requested_by_id = forms.ModelChoiceField(label=u"Requested by",queryset=RequestUser.objects.all())
    content = forms.CharField(widget=forms.Textarea,label=u"Content")

class SearchTicketForm(forms.Form):
    query = forms.CharField(label="",initial="Find",required=False)
    project_id = forms.ModelChoiceField(queryset=Project.objects.all(),label="",required=False)