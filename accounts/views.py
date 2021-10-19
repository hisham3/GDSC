from os import name
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Projects
from django.template.defaulttags import register

# Create your views here.

def home(request):
    
    return render(request, 'accounts/home.html')

def about(request):
    valid_query = {k: request.GET[k] for k in request.GET if request.GET[k]}
    
    projects = Projects.objects.all()
    
    return render(request, 'accounts/about.html', context={'projects':projects})


@register.filter(name='hesham')
def rws(a,s):
    return f'{a}{s}100'
