from wsgiref.util import request_uri
from django.shortcuts import render, HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request, 'home.html')


def feed_vehiculo(request):
    return render(request, 'vehiculos/feed_vehiculo.html')