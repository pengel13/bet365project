from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'fone',)  # campo que será mostrado
    ordering = ('-id',)  # acrescentado o menos(-) ele ordena de forma decrescente
    list_filter = ('created_date', )  # campo que vai ter filtros
    search_fields = ('id', 'first_name', 'last_name', )  # campos que serão buscados pela pesquisa
    list_per_page = 5# quantos items por page
    list_max_show_all = 100  # máximo de itens por página 
    list_editable = ( 'fone', ) # valores que poderão ser editados direto na tabela
    list_display_links = ('id', 'first_name', ) # o que está na tupla list_editable não pode estar aqui

