from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_guias, name='get_guias'),
    path('<str:prov>', views.get_guia_prov, name='get_guias'),
    path('<str:prov>/<str:localidad>', views.get_data, name='get_data'),
]




