from django.shortcuts import render
from .models import DatoHuerfanoTelefono, DatoHuerfanoCelular, DatoHuerfanoEmail
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.serializers import serialize
import json


def datosh(request):
    return render(request, 'datosh.html')


def data_type(request):

    data_types = ['celular', 'email', 'telefono']

    data = {'types': [{'value': item, 'text': item} for item in data_types]}
    return JsonResponse(data)



def data_tags(request, data_type):
    if data_type == 'celular':
        tags = DatoHuerfanoCelular.objects.values_list(
            'tag', flat=True).distinct()
    elif data_type == 'telefono':
        tags = DatoHuerfanoTelefono.objects.values_list(
            'tag', flat=True).distinct()
    else:
        tags = DatoHuerfanoEmail.objects.values_list(
            'tag', flat=True).distinct()

    tags_list = [{"value": tag, "text": tag} for tag in tags]
    tags_list.insert(0, {"value": "Todos", "text": "Todos"})
    return JsonResponse({'types': tags_list})


def view_data(request, data_type, tag):

    if data_type == 'celular':
        data_model = DatoHuerfanoCelular
    elif data_type == 'telefono':
        data_model = DatoHuerfanoTelefono
    else:
        data_model = DatoHuerfanoEmail

    if tag == 'Todos':
        data = data_model.objects.all()
    else:
        data = data_model.objects.filter(tag=tag)

    data_serialized = serialize('json', data, fields=(
        'pk', 'seccion_nombre', 'distrito_nombre', 'tag'))
    json_data = json.loads(data_serialized)
    response_data = [{data_type: item['pk'], **item['fields']}
                     for item in json_data]  

    response_data = {'data': response_data}
    return JsonResponse(response_data, safe=False)

