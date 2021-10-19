from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timedelta, datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='images', null=True)
    brief_describe = models.CharField(max_length=100, blank=True, null=True, verbose_name='Description')
    
class Projects(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    demo = models.CharField(max_length=1000, blank=True)
    repos = models.CharField(max_length=1000, blank=True)
    team = models.CharField(max_length=100, blank=True)
    finish_time = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
