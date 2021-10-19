from django.urls import path
from accounts.views import home, about

urlpatterns = [
    path('', view=home, name='home'),
    path('about', view=about, name='about')
]