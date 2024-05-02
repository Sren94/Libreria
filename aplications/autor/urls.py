from django.contrib import admin
from django.urls import path
from . import views
app_name='autor_app'
urlpatterns = [
    path(
        'ListaAutores/',
        views.authorList.as_view(),
        name='ListaAutores'),
    path(
        'BuscarAutores/',
        views.SearchAuthoorList.as_view(),
        name='BuscarAutores'
        ),
]
