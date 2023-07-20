from django.shortcuts import render
from django.http import HttpResponse
from .models import DatosPoligonos
import logging
import json
import sys


# Create your views here.

def form(request):
    template_name = 'form.html'
    return render(request, template_name)


def home(request):
    template_name = 'home.html'
    return render(request, template_name)


def filtrar_datos(request):
    if request.method == 'POST':
        provincia = request.POST.get('provincia')
        seccion = request.POST.get('seccion')
        feedback = request.POST.get('feedback')

        # Imprime los valores de los campos para verificar
        # print("Provincia:", provincia)
        # print("Cordon:", Cordon)
        # print("Feedback:", feedback)

       # Realiza la consulta a la base de datos con los parámetros de filtro
        datos_filtrados = DatosPoligonos.objects.all()

        # Filtrar por provincia solo si se selecciona "Todas las secciones"
        if seccion == "TODAS" and provincia:
            datos_filtrados = datos_filtrados.filter(distrito_nombre=provincia)
        elif seccion:
            datos_filtrados = datos_filtrados.filter(seccion_nombre=seccion)
        # print(type(datos_filtrados.))
        contador = 0
        datos_parseados = []
        for dato in datos_filtrados:
            datos_parseados.append(dato.model_to_dict())
            if contador == 0:
                contador = 1
                for i, j in dato.model_to_dict().items():
                    print(i, " ", j)

        return render(request, 'tabla.html', {'datos': datos_parseados})

    # Si no se envió un formulario, muestra el formulario vacío
    return render(request, 'form.html')
