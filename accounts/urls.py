from django.urls import path
from accounts.views import home, about, resume

urlpatterns = [
    path('', view=home, name='home'),
    path('about', view=about, name='about'),
    path('resume', view=resume, name='resume')
]
