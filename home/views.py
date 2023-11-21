from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# function based views
def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Página inicial <br>do projeto das <b>bets</b>")