from __future__ import unicode_literals

from django.db import models

class UserModel(models.Model):
    user_fname = models.CharField(max_length=40)
    user_lname  = models.CharField(max_length=40)
    user_email     = models.EmailField(max_length=200,blank=True)
    user_passwd    = models.CharField(max_length=80)

class EventModel(models.Model):
    event_title = models.CharField(max_length=40)
    event_desc  = models.CharField(max_length=40)
    event_venue = models.CharField(max_length=80)
    
