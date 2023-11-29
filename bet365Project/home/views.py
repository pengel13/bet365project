from django.shortcuts import render
from django.http import HttpResponse, HttpRequest



# function based views
def home_view(request: HttpRequest) -> HttpResponse:
    context = {"text": "Página incial do projeto das bets porém feito com context. FODA!"}
    return render(
        request,
        "home/index.html",
        
        context=context,
    )
