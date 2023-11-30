
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:id>/', view=views.contact, name='single_contact'),
    path('search/', view=views.search, name='search')
]
