from django.db import models
from django.forms.models import model_to_dict

# Create your models here.
class DatosPoligonos(models.Model):
    class Meta:
        db_table = 'poligonos_informe_front'
    
    ID_poligono = models.IntegerField(primary_key=True)
    distrito = models.IntegerField()
    distrito_nombre = models.CharField(max_length=50)
    seccion = models.IntegerField()
    seccion_nombre = models.CharField(max_length=100)
    score_promedio = models.FloatField()
    cant_personas = models.IntegerField()
    q_estimada = models.IntegerField()
    cant_personas_prio = models.IntegerField()
    indice_geo = models.FloatField()
    indice_hogar = models.FloatField()
    cant_hogares = models.IntegerField()
    observado = models.IntegerField()
    # SHAPE = models.TextField()
    shape_texto = models.TextField()

    def model_to_dict(self):
        
        data = {
            'ID_poligono': self.ID_poligono,
            'distrito': self.distrito,
            'distrito_nombre': self.distrito_nombre,
            'seccion': self.seccion,
            'seccion_nombre': self.seccion_nombre,
            'score_promedio': self.score_promedio,
            'cant_personas': self.cant_personas,
            'cant_personas_prio': self.cant_personas_prio,
            'q_estimada': self.q_estimada,
            'indice_hogar': self.indice_hogar,
            'cant_hogares': self.cant_hogares,
            'observado': self.observado,
            'shape_texto': self.shape_texto
            
        }
        
        data['indice_geo'] = round(self.indice_geo, 1)
        data['indice_hogar'] = round(self.indice_hogar, 1)
        return data

    
    def __str__(self):
        return f"{self.ID_poligono}) {self.distrito_nombre} {self.distrito_nombre}"
    