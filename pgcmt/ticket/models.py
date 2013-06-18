from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Project(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
    	return self.name

# Create your models here.
class Ticket(models.Model):
    user_id = models.ForeignKey(User)
    project_id = models.ForeignKey(Project)
    created_at = models.DateTimeField(default=datetime.now)
    content = models.TextField()
