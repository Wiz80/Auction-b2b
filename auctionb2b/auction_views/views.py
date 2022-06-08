from wsgiref.util import request_uri
from django.shortcuts import render, HttpResponse,redirect
from django.forms.models import model_to_dict

from usuarios.models import Cuenta, Vehiculo_Subasta, Foto_Vehiculo, Info_Subasta

import datetime
# Create your views here.

def index(request):
    return render(request, 'home.html')


def vehiculo(request, pk_vehiculo):
    vehiculo_model = Vehiculo_Subasta.objects.get(pk = pk_vehiculo)
    vehiculo = model_to_dict(vehiculo_model)
    cuenta = Cuenta.objects.get(pk = vehiculo_model.cuenta.user.pk)
    modelo = vehiculo_model.modelo
    fotos = [f for f in Foto_Vehiculo.objects.filter(cuenta = cuenta) if str(f.vehiculo) == modelo]       
    subasta = model_to_dict(Info_Subasta.objects.get(cuenta = cuenta, vehiculo = vehiculo_model))
    
    vehiculo_valid = {}
    for key, value in vehiculo.items():
        if key[0:6] == 'estado':
            key = f'estado {key[7:]}'
        if key[0:9] == 'especific':
            key = 'especificaciones adicionales'
        if key[0:5] == 'fecha':
            key = f'fecha {key[6:]}'
        if key == 'tecno':
            key = 'revisión tecnomecánica'
        
        vehiculo_valid[key] = value

    return render(request, 
                  'vehiculos/vehiculo.html',
                  {'vehiculo': vehiculo_valid,
                   'photos': fotos,
                   'photo_1': fotos[0],
                   'cuenta': cuenta,
                   'marca': vehiculo['marca'],
                   'modelo': modelo,
                   'precio': subasta['precio'],
                   'inicio': subasta['fecha_inicio'],
                   'cierre': subasta['fecha_cierre']})