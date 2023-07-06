import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import DatosPoligonosTexto

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file = options['csv_file']
        df = pd.read_csv(csv_file, delimiter=';', na_values=None)
        df.fillna(value={'nombre_seccion': '', 'localidad': '', 'observado': False, 'score_promedio': 0.0, 'indice_hogares': 0.0, 'hogares_estimados': 0.0}, inplace=True)
        df.replace({np.nan: None}, inplace=True)

        for _, row in df.iterrows():
            datos_poligono = DatosPoligonosTexto(
                id_poligono=int(row['id_poligono']),
                id_distrito=int(row['id_distrito']),
                nombre_distrito=row['nombre_distrito'],
                provincia=row['provincia'],
                id_seccion=int(row['id_seccion']),
                nombre_seccion=row['nombre_seccion'],
                localidad=row['localidad'],
                score_promedio=float(row['score_promedio'] or 0.0),
                q_geo=int(row['q_geo']),
                indice_geo=float(row['indice_geo'] or 0.0),
                q_estimada=float(row['q_estimada'] or 0.0),
                q_personaspriorizadas=int(row['q_personaspriorizadas']),
                indice_hogares=float(row['indice_hogares'] or 0.0),
                hogares_estimados=float(row['hogares_estimados'] or 0.0),
                observado=bool(row['observado']),
                shape_texto=row['shape_texto'],
            )
            datos_poligono.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))