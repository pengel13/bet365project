from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("search/", view=views.search, name="search"),

    # contact(CRUD)
    # READ:
    path("contact/<int:id>/detail/", view=views.contact, name="contact"),
    path("contact/create", view=views.create_contact, name='create_contact')
]

#     # CREATE
#     path("contact/create/", view=views.contact, name="contact"),
#     # UPDATE
#     path("contact/<int:id>/update/", view=views.contact, name="contact"),
#     # DELETE
#     path("contact/<int:id>/delete/", view=views.contact, name="contact"),
# ]
