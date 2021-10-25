from django.urls import path
from accounts.views import home, portfolio, resume, portfolio_view

urlpatterns = [
    path('', view=home, name='home'),
    path('resume', view=resume, name='resume'),
    path('portfolio', view=portfolio, name='portfolio'),
    path('portfolio/<int:id>', view=portfolio_view, name='portfolio_view')
]