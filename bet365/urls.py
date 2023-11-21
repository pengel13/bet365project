from django.urls import path
from .views import bet365_view, bets

urlpatterns = [
    path("bets/", bets),
    path('', bet365_view)
]
