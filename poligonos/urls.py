from django.shortcuts import render
from django.urls import path
from .views import form, user_login, user_logout, poligonos, filtrar_datos,home 

# Create your views here.

urlpatterns = [
    path('home/', home, name='home'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('poligonos/', poligonos, name='poligonos'),
    path('form/', form, name="form"),
    path('tabla/', filtrar_datos, name='tabla'),
]