# -*- coding: utf-8 -*-
from django import forms
from django.db import models
#from cover.models import Cover

class CreateProjectForm(forms.Form):
	"""
		Upload a new Cover Form
	"""
	name = forms.CharField(label=u"Project")
	#created_at = forms.DateTimeField(label=u"Date")
class CreateTicketForm(forms.Form):
	project_id = forms.CharField(label=u"Project")
	content = forms.CharField(widget=forms.Textarea,label=u"Content")