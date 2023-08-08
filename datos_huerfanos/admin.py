from django.contrib import admin
from .models import DatoHuerfanoCelular, DatoHuerfanoTelefono , DatoHuerfanoEmail
# Register your models here.
class DatoHuerfanoCelularAdmin(admin.ModelAdmin):
    list_filter = ('tag',)

admin.site.register(DatoHuerfanoCelular, DatoHuerfanoCelularAdmin)
admin.site.register(DatoHuerfanoEmail)
admin.site.register(DatoHuerfanoTelefono)