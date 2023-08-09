from django.shortcuts import render, redirect
from .models import DatosPoligonos
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.
@login_required
def home(request):
    template_name = 'home.html'
    return render(request, template_name)

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
def form(request):
    template_name = 'form.html'
    return render(request, template_name)

@login_required
def poligonos(request):
    template_name = 'poligonos.html'
    return render(request, template_name)

@login_required
def filtrar_datos(request):
    if request.method == 'POST':
        provincia = request.POST.get('provincia')
        seccion = request.POST.get('seccion')
        feedback = request.POST.get('feedback')

        datos_filtrados = DatosPoligonos.objects.all()

        
        if seccion == "TODAS" and provincia:
            datos_filtrados = datos_filtrados.filter(distrito_nombre=provincia)
        elif seccion:
            datos_filtrados = datos_filtrados.filter(seccion_nombre=seccion)
        
        contador = 0
        datos_parseados = []
        for dato in datos_filtrados:
            datos_parseados.append(dato.model_to_dict())
            if contador == 0:
                contador = 1
                for i, j in dato.model_to_dict().items():
                    print(i, " ", j)

        return render(request, 'tabla.html', {'datos': datos_parseados})

    
    return render(request, 'form.html')
