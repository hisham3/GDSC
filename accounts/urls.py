from django.urls import path
from accounts.views import home, portfolio

urlpatterns = [
    path('', view=home, name='home'),
    path('portfolio', view=portfolio, name='portfolio')
]