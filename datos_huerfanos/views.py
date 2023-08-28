from django.shortcuts import render
from .models import DatoHuerfanoTelefono, DatoHuerfanoCelular, DatoHuerfanoEmail
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.contrib.auth.decorators import login_required

from .tests import *


@login_required
def datosh(request):
    
    return render(request, 'datosh.html')


@login_required
def data_type(request):

    data_types = ['celular', 'email', 'telefono']

    data = {'types': [{'value': item, 'text': item} for item in data_types]}
    return JsonResponse(data)


@login_required
def get_distritos(request, data_type):

    total_data = []
    for i in data_type:
        if i == 't':
            filtered_data = DatoHuerfanoTelefono.objects.values_list(
                'distrito_nombre').distinct()
            total_data += filtered_data
        elif i == 'c':
            filtered_data = DatoHuerfanoCelular.objects.values_list(
                'distrito_nombre').distinct()
            total_data += filtered_data
        elif i == 'e':
            filtered_data = DatoHuerfanoEmail.objects.values_list(
                'distrito_nombre').distinct()
            total_data += filtered_data
    
    distritos = [{"value": filter[0], "text": filter[0]}
                 for filter in set(total_data)]
    distritos.insert(0, {"value": "Todos", "text": "Todos"})

    return JsonResponse({'types': distritos})


def data_tags(request, data_type, distrito):

    total_data = []

    index = distrito.find('_')
    if distrito == 'caba':
        distrito = distrito.upper()
    elif index != -1:
        distrito = distrito.replace('_', ' ').title()
    else:
        distrito = distrito.capitalize()

    for i in data_type:
        if i == 'c':
            if distrito == 'Todos':
                tags = DatoHuerfanoCelular.objects.values_list(
                    'tag', flat=True).distinct()
            else:
                tags = DatoHuerfanoCelular.objects.filter(
                    distrito_nombre=distrito).values_list('tag', flat=True).distinct()
        elif i == 't':
            if distrito == 'Todos':
                tags = DatoHuerfanoTelefono.objects.values_list(
                    'tag', flat=True).distinct()
            else:
                tags = DatoHuerfanoTelefono.objects.filter(
                    distrito_nombre=distrito).values_list('tag', flat=True).distinct()
        elif i == 'e':
            if distrito == 'Todos':
                tags = DatoHuerfanoEmail.objects.values_list(
                    'tag', flat=True).distinct()
            else:
                tags = DatoHuerfanoEmail.objects.filter(
                    distrito_nombre=distrito).values_list('tag', flat=True).distinct()
        total_data += tags


    tags_list = [{"value": tag, "text": tag} for tag in set(total_data)]
    tags_list.insert(0, {"value": "Todos", "text": "Todos"})
    return JsonResponse({'types': tags_list})



def get_data_for_type(data_model, distrito, tag):
    data = data_model.objects.all()
    
    if distrito != 'Todos':
        data = data.filter(distrito_nombre=distrito)
    if tag != 'Todos':
        data = data.filter(tag=tag)

    return list(data.values('pk', 'seccion_nombre', 'distrito_nombre', 'tag'))

@login_required
def view_data(request, data_type, distrito, tag):
    # Preprocesamiento del distrito
    index = distrito.find('_')
    if distrito == 'caba':
        distrito = distrito.upper()
    elif index != -1:
        distrito = distrito.replace('_', ' ').title()
    else:
        distrito = distrito.capitalize()

    response_data = {'celular': [], 'telefono': [], 'email': []}

    type_to_model_map = {
        'c': DatoHuerfanoCelular,
        't': DatoHuerfanoTelefono,
        'e': DatoHuerfanoEmail
    }

    type_to_key_map = {
        'c': 'celular',
        't': 'telefono',
        'e': 'email'
    }

    for dtype in data_type:
        model = type_to_model_map.get(dtype)
        key = type_to_key_map.get(dtype)

        if model and key:
            response_data[key] = get_data_for_type(model, distrito, tag)


    return JsonResponse(response_data, safe=False)



