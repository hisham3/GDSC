from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.utils.timezone import timedelta, datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='images', null=True)
    brief_describe = models.CharField(max_length=100, blank=True, null=True, verbose_name='Description')
    
class Projects(models.Model):
    
    choices = [
        ['small','small'],
        ['medium','medium'],
        ['huge','huge'],
    ]
    
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    level = models.CharField(max_length=500, choices=choices, null=True)
    demo = models.CharField(max_length=1000, blank=True)
    members = models.ManyToManyField(to=User, related_name='participated', blank=True)
    finish_time = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Resume(models.Model) :
    choices = [
        ['Experience','Experience'],
        ['Education','Education'],
        ['Volunteering','Volunteering'],
    ]
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500)
    year = models.IntegerField()
    section = models.CharField(max_length=500, choices=choices, null=True)
    active = models.BooleanField(default=False)
    place = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Resumes"

    

class Contact(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    
    def __str__(self):
        return self.title