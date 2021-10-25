from os import name
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Projects
from django.template.defaulttags import register

# Create your views here.

def home(request):
    
    return render(request, 'accounts/home.html')

def portfolio(request):
    
    projects = Projects.objects.all()
    
    if request.method == 'GET':
        
        if request.GET.get('search'):
            print('1'*50)
            projects = projects.filter(name__icontains=request.GET.get('search'))
        
        if request.GET.get('level_select') != 'all' and request.GET.get('level_select'):
            projects = projects.filter(level=request.GET.get('level_select'))
    
    return render(request, 'accounts/portfolio.html', context={'projects':projects})

def portfolio_view(request, id):
    
    projects = get_object_or_404(Projects, pk=id)
    
    return render(request, 'accounts/portfolio_view.html', context={'projects':projects})

def resume(request):
    return render(request, 'accounts/resume.html')


@register.filter(name='hesham')
def rws(a,s):
    return f'{a}{s}100'
