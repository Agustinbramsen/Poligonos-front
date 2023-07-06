from django.shortcuts import render
from django.http import HttpResponse
from core.models import DatosPoligonosTexto
import logging
import json


# Create your views here.

def form (request):
    template_name = 'form.html'
    return render(request, template_name)

def home (request):
    template_name = 'home.html'
    return render(request, template_name)

def filtrar_datos(request):
    if request.method == 'POST':
        provincia = request.POST.get('provincia')
        Cordon = request.POST.get('Cordon')
        feedback = request.POST.get('feedback')

        # Imprime los valores de los campos para verificar
        print("Provincia:", provincia)
        print("Cordon:", Cordon)
        print("Feedback:", feedback)

        # Realiza la consulta a la base de datos con los parámetros de filtro
        datos_filtrados = DatosPoligonosTexto.objects.all()
        if provincia:
            datos_filtrados = datos_filtrados.filter(provincia=provincia)
        if Cordon:
            datos_filtrados = datos_filtrados.filter(nombre_distrito=Cordon)

        # Imprime los datos filtrados para verificar
        for dato in datos_filtrados:
            print("ID Polígono:", dato.id_poligono)
            print("ID Distrito:", dato.id_distrito)
            # Imprime los demás campos que deseas mostrar en la tabla

        # Devuelve los resultados en una tabla
        return render(request, 'tabla.html', {'datos': datos_filtrados})

    # Si no se envió un formulario, muestra el formulario vacío
    return render(request, 'form.html')