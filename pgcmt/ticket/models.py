from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Project(models.Model):
    name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=250)
    def __unicode__(self):
    	return self.name


class RequestUser(models.Model):
    username = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return self.username

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    requested_by = models.ForeignKey(RequestUser)
    created_at = models.DateTimeField(default=datetime.now)
    content = models.TextField()