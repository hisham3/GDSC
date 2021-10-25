from django.urls import path
from accounts.views import home, portfolio, resume

urlpatterns = [
    path('', view=home, name='home'),
    path('resume', view=resume, name='resume'),
    path('portfolio', view=portfolio, name='portfolio')
]