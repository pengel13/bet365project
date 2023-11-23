from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from bet365.data import posts
from typing import Any

def bet365_view(request: HttpRequest) -> HttpResponse:
    context = {
        "text": "Aqui tem alguns insights sobre as bets feitas na casa de apostas da bet365",
        "title": "bet365 Home Page",
    }
    return render(request, "bet365/home.html", context=context)


def bets(request: HttpRequest) -> HttpResponse:
    context = {
        "text": "Aqui tem todas as bets já realizadas na bet365",
        "title": "bet365 All bets",
        "posts": posts,
    }
    return render(request, "bet365/bet365.html", context=context)


def post(request: HttpRequest, id: int) -> HttpResponse:
    found_post:dict[str, Any] | None= None
    post_id = 0
    for p in posts:
        if p["id"] == id:
            found_post = p
            post_id= p['id']
            break

    if found_post is None:
        raise Http404("Post não existe.")
    context = {
        "text": f"Bet de id {post_id}",
        "title": "- " +  found_post['title'],
        "post": found_post
    }
    return render(request, "bet365/bet365.html", context=context)
