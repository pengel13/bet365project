from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from contact.forms import ContactForm


def create_contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        context = {"form": ContactForm(request.POST)}
        return render(request, "contact/create.html", context)

    context = {"form": ContactForm(), 'site_title': "Create Contact", }
    return render(request, "contact/create.html", context)
