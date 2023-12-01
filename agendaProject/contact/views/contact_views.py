from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    contacts = Contact.objects.filter(show=True).order_by("-id")
    # print(contacts.query)
    """
    SELECT "contact_contact"."id",
    "contact_contact"."first_name",
    "contact_contact"."last_name",
    "contact_contact"."fone",
    "contact_contact"."email",
    "contact_contact"."created_date",
    "contact_contact"."description",
    "contact_contact"."show",
    "contact_contact"."picture",
    "contact_contact"."category_id",
    "contact_contact"."owner_id"
    FROM "contact_contact"
    WHERE "contact_contact"."show"
    ORDER BY "contact_contact"."id" DESC
    """
    # o filter funciona como um where
    # só retornará onde o field show for igual a True
    paginator = Paginator(contacts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "site_title": "Contatos"}

    return render(request, "contact/index.html", context=context)


def search(request: HttpRequest) -> HttpResponse:
    search_value = request.GET.get("q", "").strip()
    if len(search_value) == 0:
        return redirect("contact:index")

    contacts = (
        Contact.objects.filter(show=True)
        .filter(
            Q(first_name__icontains=search_value)
            | Q(fone__icontains=search_value)
            | Q(email__icontains=search_value)
            | Q(last_name__icontains=search_value)
        )
        .order_by("-id")[:50]
    )
    # __icontains é um lookup. ver mais na documentação

    paginator = Paginator(contacts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "site_title": "Search",
        "search_value": search_value,
    }

    return render(request, "contact/index.html", context=context)


def contact(request: HttpRequest, id: int) -> HttpResponse:
    single_contact = Contact.objects.filter(id=id, show=True).first()
    if single_contact is None:
        raise Http404("ID não existe ou está invisível")
    title = f"{single_contact.first_name} {single_contact.last_name}"
    # metódo django.shortcuts.get_object_or_404
    context = {"contact": single_contact, "site_title": title}  # type: ignore
    return render(request, "contact/contact.html", context)
