from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



guias_telefonicas = {
    'buenos_aires': GuiaTelefonicaBuenosaires,
    'caba': GuiaTelefonicaCaba,
    'catamarca': GuiaTelefonicaCatamarca,
    'chaco': GuiaTelefonicaChaco,
    'chubut': GuiaTelefonicaChubut,
    'cordoba': GuiaTelefonicaCordoba,
    'corrientes': GuiaTelefonicaCorrientes,
    'entre_rios': GuiaTelefonicaEntrerios,
    'formosa': GuiaTelefonicaFormosa,
    'jujuy': GuiaTelefonicaJujuy,
    'la_pampa': GuiaTelefonicaLapampa,
    'la_rioja': GuiaTelefonicaLarioja,
    'mendoza': GuiaTelefonicaMendoza,
    'misiones': GuiaTelefonicaMisiones,
    'neuquen': GuiaTelefonicaNeuquen,
    'rio_negro': GuiaTelefonicaRionegro,
    'salta': GuiaTelefonicaSalta,
    'san_juan': GuiaTelefonicaSanjuan,
    'san_luis': GuiaTelefonicaSanluis,
    'santa_cruz': GuiaTelefonicaSantacruz,
    'santa_fe': GuiaTelefonicaSantafe,
    'santiago_del_estero': GuiaTelefonicaSantiagodelestero,
    'tierra_del_fuego': GuiaTelefonicaTierradelfuego,
    'tucuman': GuiaTelefonicaTucuman
}

@login_required
def get_guias(request):
    keys_list = [{'value': key.lower(), 'text': key.lower()} for key in guias_telefonicas.keys()]
    return JsonResponse({'types': keys_list}, safe=False)

@login_required
def get_guia_prov(request, prov):
    GuiaClass = guias_telefonicas.get(prov.lower())

    localidades = GuiaClass.objects.values('localidad').distinct()  
    localidades_list = [{'value': item['localidad'], 'text': item['localidad']} for item in localidades]

    return JsonResponse({'types': localidades_list})
@login_required

def get_data(request, prov, localidad):
    GuiaClass = guias_telefonicas.get(prov.lower())
    print(localidad)
    if localidad == 'undefined':
            guias = GuiaClass.objects.filter(localidad='?').values()
    else:
            guias = GuiaClass.objects.filter(localidad=localidad).values()
    

    # guias = GuiaClass.objects.filter(localidad=localidad).values()

    data = [
        {
            'tipoguia': item['tipoguia'],
            'titular': item['titular'],
            'telefono': item['telefono'],
            'direccion': item['direccion'],
            'localidad': item['localidad'],
            'provincia': item['provincia'],
            'rubro': item['rubro'],
            'partido': item['partido']
        }
        for item in guias
    ]
    return JsonResponse({'data': data})


