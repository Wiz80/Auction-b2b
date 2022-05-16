#API - marcas carros, motos, etc
from bs4 import BeautifulSoup
import requests

class Vehiculo():

    def __init__(self, url, categoria):
        self.categoria = categoria
        self.url = url

    def get_vehiculo(self):
   
        url = self.url     
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        
        page_marcas = requests.get(url, headers=headers)
        soup_marcas = BeautifulSoup(page_marcas.content, 'html.parser')

        if self.categoria == 1:
            marcas_carros = soup_marcas.find_all('a', {'class': 'marca'})
            marcas = [marca.text for marca in marcas_carros]

        if self.categoria == 2:
            select_tag = soup_marcas.find_all('select', {'class': 'selectfield'})
            marcas = [select.text for select in select_tag if select['id'] == 'f_marca']
            marcas = marcas[0].split("\n")[2:-1]
        
        if self.categoria == 4:
            marcas = "DODGE--HINO--GMC--FREIGHTLINER--FORD--WESTERN STAR TRUCK--CHEVROLET--KENWORTH--ISUZU--INTERNATIONAL--SCANIA--PETERBILT--MITSUBISHI--MACK--VOLVO--Daf Trucks--Man--Mercedes Benz--Renault--Nissan"
            marcas = sorted(dict.fromkeys([marca.lower().capitalize() for marca in marcas.split("--")]))
            

        dict_marcas = {marca[0]:[] for marca in marcas}
        for marca in marcas:
            dict_marcas[marca[0]].append(marca)
        
        return dict_marcas