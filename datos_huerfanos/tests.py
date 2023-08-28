from django.test import TestCase
from .models import *

def test_distrito(data_type):
    total_data = []
    for i in data_type:
        if i == 't':
            filtered_data = DatoHuerfanoTelefono.objects.values_list(
                'distrito_nombre').distinct()
            total_data += filtered_data
        elif i == 'c':
            filtered_data = DatoHuerfanoCelular.objects.values_list(
                'distrito_nombre').distinct()
            total_data += filtered_data
        elif i == 'e':
            filtered_data = DatoHuerfanoEmail.objects.values_list(
                'distrito_nombre').distinct()
            total_data += filtered_data
    total_data = set(total_data)
    print((total_data))

test_distrito('t')
test_distrito('tc')
test_distrito('tce')
test_distrito('te')

