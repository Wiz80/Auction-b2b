from wsgiref.util import request_uri
from django.shortcuts import render, HttpResponse,redirect
from bs4 import BeautifulSoup
import requests

# Create your views here.

url_marcas_carros = "https://motorgiga.com/marcas-de-coches"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page_marcas_carros = requests.get(url_marcas_carros, headers=headers)
soup_marcas = BeautifulSoup(page_marcas_carros.content, 'html.parser')
#Marcas Carros
#marcas_carros = soup_marcas.find_all(lambda tag:tag.name=="a" and hasattr(tag, "class") and "marca" in tag['class'])
marcas_carros = soup_marcas.find_all('a', {'class': 'marca'})
marcas = [marca.text for marca in marcas_carros]

dict_marcas = {marca[0]:[] for marca in marcas}
for marca in marcas:
    dict_marcas[marca[0]].append(marca)

def index(request):
    return render(request, 'subastar_step_2.html', {'marcas': dict_marcas})
