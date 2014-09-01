from django.db import models
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label=u"Username",max_length=100)
    password = forms.CharField(label=u"Password",widget=forms.PasswordInput(render_value=False),max_length=100)
    next = forms.CharField(widget=forms.widgets.HiddenInput())

class ChangePasswordForm(forms.Form):
    password = forms.CharField(label=u"Password",widget=forms.PasswordInput(render_value=False),max_length=100)
    password_check = forms.CharField(label=u"Password check",widget=forms.PasswordInput(render_value=False),max_length=100)