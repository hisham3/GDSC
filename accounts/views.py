from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'accounts/home.html')

def portfolio(request):
    
    return render(request, 'accounts/portfolio.html')

def portfolio_view(request, id):

    return render(request, 'accounts/portfolio_view.html')

def resume(request):

    return render(request, 'accounts/resume.html',)

def contacts(request):
    
    return render(request, 'accounts/contacts.html')
