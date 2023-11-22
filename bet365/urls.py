from django.urls import path
from .views import bet365_view, bets

app_name= 'bet365'

urlpatterns = [
    path('', bet365_view, name = "home"),
    path("bets/", bets, name = "allBets"),

]
