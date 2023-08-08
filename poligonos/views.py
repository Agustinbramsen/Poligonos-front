from django.shortcuts import render
from .models import DatosPoligonos



# Create your views here.

def home(request):
    template_name = 'home.html'
    return render(request, template_name)

def form(request):
    template_name = 'form.html'
    return render(request, template_name)


def poligonos(request):
    template_name = 'poligonos.html'
    return render(request, template_name)


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
