# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from ticket.views import Project,RequestUser,Ticket
from django.contrib.auth.models import User


from django.forms import ModelForm, Textarea,Select

#from cover.models import Cover

#class CreateProjectForm(forms.Form):
#    name = forms.CharField(label=u"Project")
#    description = forms.CharField(label=u"Description",widget=forms.Textarea)

class CreateProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name','description']
        widgets = { 'description': Textarea()}      


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["project","requested_by","content"]
        widgets = {'project':Select(),'requested_by':Select()}

#class CreateTicketForm(forms.Form):
#    project_id = forms.ModelChoiceField(label=u"Project",queryset=Project.objects.all())
#    requested_by_id = forms.ModelChoiceField(label=u"Requested by",queryset=RequestUser.objects.all())
#    content = forms.CharField(label=u"Content",widget=forms.Textarea)

class SearchTicketForm(forms.Form):
    query = forms.CharField(label="",initial="Find",required=False)
    project_id = forms.ModelChoiceField(queryset=Project.objects.all(),label="",required=False)

#class CreateRequestUser(forms.Form):
#    name = forms.CharField(label=u"Name Surname",required=True)

class CreateRequestUser(ModelForm):
   class Meta:
        model = RequestUser
        fields = ["username"]