from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def bet365_view(request: HttpRequest) -> HttpResponse:
    context= {"text": "Aqui tem alguns insights sobre as bets feitas na casa de apostas da bet365", 'title': 'bet365 Home Page'}
    return render(request, 'bet365/home.html', context = context)

def bets(request: HttpRequest) -> HttpResponse:
    context= {"text": "Aqui tem todas as bets já realizadas na bet365", 'title': 'bet365 All bets'}
    return render(request, 'bet365/bet365.html', context = context)