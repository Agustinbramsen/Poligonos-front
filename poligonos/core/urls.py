from django.shortcuts import render
from django.urls import path
from .views import form, home, filtrar_datos

# Create your views here.

urlpatterns = [
    path('home/', home, name='home'),
    path('form/', form, name="form"),
    path('tabla/', filtrar_datos, name='tabla'),
]