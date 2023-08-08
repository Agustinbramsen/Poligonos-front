from django.shortcuts import render
from django.urls import path
from .views import form, poligonos, filtrar_datos,home

# Create your views here.

urlpatterns = [
    path('', home, name='home'),
    path('poligonos/', poligonos, name='poligonos'),
    path('form/', form, name="form"),
    path('tabla/', filtrar_datos, name='tabla'),
]