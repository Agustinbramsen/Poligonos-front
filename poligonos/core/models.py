from django.db import models

# Create your models here.
class DatosPoligonosTexto(models.Model):
    id_poligono = models.IntegerField(primary_key=True)
    id_distrito = models.SmallIntegerField()
    nombre_distrito = models.CharField(max_length=50)
    provincia = models.CharField(max_length=100)
    id_seccion = models.IntegerField()
    nombre_seccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=254)
    score_promedio = models.FloatField()
    q_geo = models.BigIntegerField()
    indice_geo = models.DecimalField(max_digits=24, decimal_places=4)
    q_estimada = models.DecimalField(max_digits=28, decimal_places=4)
    q_personaspriorizadas = models.BigIntegerField()
    indice_hogares = models.FloatField()
    hogares_estimados = models.FloatField()
    observado = models.BooleanField()
    shape_texto = models.TextField()