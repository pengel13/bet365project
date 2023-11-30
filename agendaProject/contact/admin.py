# flake8: noqa
from django.contrib import admin
from contact import models

# login admin
# user: pedro
# senha: 123456

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'fone', 'show')  # campo que será mostrado
    ordering = ('id',)  # acrescentado o menos(-) ele ordena de forma decrescente
    list_filter = ('created_date', )  # campo que vai ter filtros
    search_fields = ('id', 'first_name', 'last_name', )  # campos que serão buscados pela pesquisa
    list_per_page = 20  # quantos items por page
    list_max_show_all = 1000  # máximo de itens por página 
    list_editable = ( 'show', ) # valores que poderão ser editados direto na tabela
    list_display_links = ('id', 'first_name', )  # o que está na tupla list_editable não pode estar aqui

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # campo que será mostrado
    ordering = ('-id',)  # acrescentado o menos(-) ele ordena de forma decrescente
    

  