from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def bet365_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Aqui você encontra alguns insights sobre as bets feitas dentro do site da bet365")

def bets(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Aqui você encontra todas as bets já feitas na bet365")