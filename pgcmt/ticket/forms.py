# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from ticket.views import Project,RequestUser
#from cover.models import Cover

class CreateProjectForm(forms.Form):
    name = forms.CharField(label=u"Project")
    description = forms.CharField(label=u"Description",widget=forms.Textarea)

class CreateTicketForm(forms.Form):
    project_id = forms.ModelChoiceField(label=u"Project",queryset=Project.objects.all())
    requested_by_id = forms.ModelChoiceField(label=u"Requested by",queryset=RequestUser.objects.all())
    content = forms.CharField(label=u"Content",widget=forms.Textarea)

class SearchTicketForm(forms.Form):
    query = forms.CharField(label="",initial="Find",required=False)
    project_id = forms.ModelChoiceField(queryset=Project.objects.all(),label="",required=False)

class CreateRequestUser(forms.Form):
    name = forms.CharField(label=u"Name Surname",required=True)
    