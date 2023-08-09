from django.shortcuts import render, redirect
from .models import DatoHuerfanoTelefono, DatoHuerfanoCelular, DatoHuerfanoEmail
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("User authenticated:", user)
            auth_login(request, user)
            return redirect('home')
        else:
            print("Authentication failed for username:", username)
            messages.error(request, 'Credenciales inválidas. Por favor, inténtelo de nuevo.')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  


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
    if data_type == 'telefono':
        filtered_data = DatoHuerfanoTelefono.objects.values_list('distrito_nombre').distinct()
    elif data_type == 'celular':
        filtered_data = DatoHuerfanoCelular.objects.values_list('distrito_nombre').distinct()
    elif data_type == 'email':
        filtered_data = DatoHuerfanoEmail.objects.values_list('distrito_nombre').distinct()
    
    distritos = [{"value": filter[0], "text": filter[0]} for filter in filtered_data]
    distritos.insert(0, {"value": "Todos", "text": "Todos"})

    return JsonResponse({'types': distritos})


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

@login_required
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

