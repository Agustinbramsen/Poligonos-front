from django.contrib import admin
from .models import DatosPoligonos
# Register your models here.
class PoligonosAdmin(admin.ModelAdmin):
    list_filter = ['distrito_nombre', 'seccion_nombre']

admin.site.register(DatosPoligonos, PoligonosAdmin)