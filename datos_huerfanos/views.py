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



# def view_data(request, data_type, distrito, tag ):
#     print(data_type, 'data_type')
#     print(distrito, 'distrito')
#     print(tag, 'tag')

#     index = distrito.find('_')
#     if distrito == 'caba':
#         distrito = distrito.upper()
#     elif index != -1:
#         distrito = distrito.replace('_', ' ').title()
#     else:
#         distrito = distrito.capitalize()

#     if data_type == 'celular':
#         data_model = DatoHuerfanoCelular
#     elif data_type == 'telefono':
#         data_model = DatoHuerfanoTelefono
#     else:
#         data_model = DatoHuerfanoEmail

#     data = data_model.objects.all()
#     print(len(data))
#     if distrito != 'Todos':
#         data = data.filter(distrito_nombre=distrito)

#     if tag != 'Todos':
#         data = data.filter(tag=tag)
#     data_serialized = serialize('json', data, fields=(
#         'pk', 'seccion_nombre', 'distrito_nombre', 'tag'))
#     json_data = json.loads(data_serialized)
#     response_data = [{data_type: item['pk'], **item['fields']}
#                      for item in json_data]
#     print(len(response_data))
#     response_data = {'data': response_data}
#     return JsonResponse(response_data, safe=False)

# @login_required
# def view_data(request, data_type, distrito, tag):
#     # Preprocesamiento del distrito
#     index = distrito.find('_')
#     if distrito == 'caba':
#         distrito = distrito.upper()
#     elif index != -1:
#         distrito = distrito.replace('_', ' ').title()
#     else:
#         distrito = distrito.capitalize()


#     response_data = {'data': []}

#     for dtype in data_type:
#         if dtype == 'c':
#             data_model = DatoHuerfanoCelular
#         elif dtype == 't':
#             data_model = DatoHuerfanoTelefono
#         elif dtype == 'e':
#             data_model = DatoHuerfanoEmail

#         data = data_model.objects.all()

#         if distrito != 'Todos':
#             data = data.filter(distrito_nombre=distrito)
#         if tag != 'Todos':
#             data = data.filter(tag=tag)

#         data_serialized = serialize('json', data, fields=('pk', 'seccion_nombre', 'distrito_nombre', 'tag'))
#         json_data = json.loads(data_serialized)
#         # response_data['data'].extend([{dtype: item['pk'], **item['fields']} for item in json_data])
#         for item in json_data:
#             record = {dtype: item['pk'], **item['fields']}
#             response_data['data'].append(record)

#     return JsonResponse(response_data, safe=False)


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

# def view_data(request, data_type, distrito, tag):
#     # Preprocesamiento del distrito
#     index = distrito.find('_')
#     if distrito == 'caba':
#         distrito = distrito.upper()
#     elif index != -1:
#         distrito = distrito.replace('_', ' ').title()
#     else:
#         distrito = distrito.capitalize()

#     response_data = {'celular': [], 'telefono': [], 'email': []}

#     for dtype in data_type:
#         key = ''
#         if dtype == 'c':
#             data_model = DatoHuerfanoCelular
#             key = 'celular'
#         elif dtype == 't':
#             data_model = DatoHuerfanoTelefono
#             key = 'telefono'
#         elif dtype == 'e':
#             data_model = DatoHuerfanoEmail
#             key = 'email'

#         data = data_model.objects.all()
#         if distrito != 'Todos':
#             data = data.filter(distrito_nombre=distrito)
#         if tag != 'Todos':
#             data = data.filter(tag=tag)

#         data_serialized = serialize('json', data, fields=('pk', 'seccion_nombre', 'distrito_nombre', 'tag'))
#         json_data = json.loads(data_serialized)
#         for item in json_data:
#             record = {'id': item['pk'], **item['fields']}
#             response_data[key].append(record)
#         print(len(json_data))
#     return JsonResponse(response_data, safe=False)


