from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm
from contact.models import Contact


def create_contact(request: HttpRequest) -> HttpResponse:
    form_action = reverse("contact:create_contact")
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        context = {
            "form": form,
            "site_title": "Create Contact",
            "form_action": form_action,
        }

        if form.is_valid():
            print("formulário é válido")
            contact = form.save(commit=False)
            contact.show = False
            contact.save()
            return redirect("contact:update_contact", contact_id=contact.pk)

        return render(request, "contact/create.html", context)

    context = {
        "form": ContactForm(),
        "site_title": "Create Contact",
        "form_action": form_action,
    }
    return render(request, "contact/create.html", context)


def update(request: HttpRequest, contact_id) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse("contact:update_contact", args=(contact_id, ))
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            "form": form,
            "site_title": "Create Contact",
            "form_action": form_action,
        }

        if form.is_valid():
            print("formulário é válido")
            form.save()
            return redirect("contact:update_contact", contact_id=contact.pk)

        return render(request, "contact/create.html", context)

    context = {
        "form": ContactForm(instance=contact),
        "site_title": "Create Contact",
        "form_action": form_action,
    }
    return render(request, "contact/create.html", context)


def delete(request: HttpRequest, contact_id) -> HttpResponse:
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    confirmation = request.POST.get('confirmation', 'no')
    print(confirmation)
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    context = {
        'contact': contact,
        'site_title': 'Update contact',
        'confirmation': confirmation,
    }
    return render(request, 'contact/contact.html', context)
