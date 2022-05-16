from threading import excepthook
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Modelo
from django.contrib.auth.models import User
from usuarios.models import Cuenta, Vehiculo_Subasta

#Buscar departamentos y municipios
import pandas as pd
from django.contrib.staticfiles import finders

#Buscar vehiculos
from .get_vehiculos import Vehiculo

#Exceptions
from django.db.utils import IntegrityError

#Forms
from usuarios.forms import ImageUploadForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 
                         'users\login.html', 
                         {'error': 'La combinación de usuario y contraseña no es correcta.'})

    return render(request, 'users\login.html')

def signup(request):
    csv_path = finders.find('data\Departamentos_y_municipios_de_Colombia.csv')
    datos_dane = pd.read_csv(csv_path)
    departamentos = sorted(set(list(datos_dane['DEPARTAMENTO'])))
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        is_further = len(password) >= 8
        is_upper = len([i for i in password if i.isupper() == 1]) >= 1
        is_lower = len([i for i in password if i.islower() == 1]) >= 1
        is_num = len([i for i in password if i.isdigit() == 1]) >= 1
        if not(is_further and is_upper and is_lower and is_num):
            return render(request, 
                        'users/signup.html',
                        {'departamentos': departamentos,
                        'dane': datos_dane,
                        'error_pass': True})
        try: 
            user = User.objects.create_user(username = username, password = password)
        except IntegrityError:
            return render(request, 
                         'users/signup.html',
                         {'departamentos': departamentos,
                         'dane': datos_dane,
                         'error_user': 'El usuario ya ha sido creado previamente'})

        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        

        cuenta = Cuenta(user = user,
                        birth_date = request.POST['Fecha_Nacimiento'],
                        cc = request.POST['cc'],
                        departamento = request.POST['departamento'],
                        ciudad = request.POST['municipio'],
                        phone = request.POST['phone'])
        cuenta.save()

        return redirect('index')

    return render(request, 
                  'users/signup.html',
                  {'departamentos': departamentos,
                   'dane': datos_dane})


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def subastar_step_1(request):
    profile = Cuenta.objects.get(pk = request.user.pk)
    vehiculo =  Vehiculo_Subasta(cuenta = profile)    

    if request.method == 'POST':
        try:
            categoria = int(request.POST['categoria'])
            if categoria == 1:
                categoria_user = 'Carros y Camionetas'
            elif categoria == 2:
                categoria_user = 'Motos'
            elif categoria == 3:
                categoria_user = 'Autobuses'
            elif categoria == 4:
                categoria_user = 'Camiones'
            elif categoria == 5:
                categoria_user = 'Motocarros y Mototriciclos'
            elif categoria == 6:
                categoria_user = 'Otros'
            
            vehiculo.categoria = categoria_user

            vehiculo.save()
            lista_vehiculos = Vehiculo_Subasta.objects.filter(cuenta = profile) 
            if len(lista_vehiculos) > 1:
                for idx,i in reversed(list(enumerate(lista_vehiculos))):
                    if idx > 0:
                        if (list(lista_vehiculos)[-1].created - Vehiculo_Subasta.objects.filter(cuenta = profile)[idx-1].created).total_seconds() <= 1000:
                            Vehiculo_Subasta.objects.get(pk = Vehiculo_Subasta.objects.filter(cuenta = profile)[idx-1].pk).delete()
            
            return redirect('subastar_2', id=categoria)
        
        except:
            return render(request, 
                          'users/subastar_step_1.html',
                          {'error': 'Debes seleccionar una categoría'})     

    return render(request, 'users/subastar_step_1.html')

@login_required
def subastar_step_2(request,id):
    profile = Cuenta.objects.get(pk = request.user.pk)
    vehiculo = Vehiculo_Subasta.objects.filter(cuenta = profile).last()

    if request.method == 'POST':
        try:
            marca = request.POST['marca']
            if marca == "Añadir nueva marca":
                return render(request, 
                'users/subastar_step_2.html',
                {'titulo': 'Especifique la marca del vehículo',
                'dict_vehiculos_none': True,
                'id':id})
            else:
                vehiculo.marca = marca
                vehiculo.save()
                return redirect('subastar_3', id=id)

        except:
            if id == 1 or id == 2 or id == 3 or id == 4:
                if id == 1:
                    #url para marcas de carros y camionetas
                    url = "https://motorgiga.com/marcas-de-coches"

                if id == 2:
                    #url para marcas de motos
                    url = "https://www.motorbikemag.es/motos-marcas-modelos/"

                if id == 4:
                    url = None

                dict_vehiculos = Vehiculo(url, id).get_vehiculo()

                return render(request, 
                    'users/subastar_step_2.html',
                    {'titulo': 'Especifique la marca del vehículo',
                    'dict_vehiculos': dict_vehiculos,
                    'id' : id,
                    'error': 'Debes escoger una marca de vehículo'})
            else:
                return render(request, 
                'users/subastar_step_2.html',
                {'titulo': 'Especifique la marca del vehículo',
                'dict_vehiculos_none': True,
                'id':id,
                'error': 'Digita el nombre de la marca del vehículo'})


    if id == 1 or id == 2 or id == 3 or id == 4:
        if id == 1:
            #url para marcas de carros y camionetas
            url = "https://motorgiga.com/marcas-de-coches"

        if id == 2:
            #url para marcas de motos
            url = "https://www.motorbikemag.es/motos-marcas-modelos/"

        if id == 4:
            url = None

        dict_vehiculos = Vehiculo(url, id).get_vehiculo()

        return render(request, 
                    'users/subastar_step_2.html',
                    {'titulo': 'Especifique la marca del vehículo',
                    'dict_vehiculos': dict_vehiculos,
                    'id' : id})

    return render(request, 
                'users/subastar_step_2.html',
                {'titulo': 'Especifique la marca del vehículo',
                'dict_vehiculos_none': True,
                'id': id})

@login_required
def subastar_step_3(request,id):
    profile = Cuenta.objects.get(pk = request.user.pk)
    vehiculo = Vehiculo_Subasta.objects.filter(cuenta = profile).last()
    if request.method == 'POST': 
        modelo = request.POST['modelo']
        if modelo == '':
            return render(request,
                'users/subastar_step_3.html',
                {'titulo': '¿Cuál es el modelo del vehículo?',
                'id':id,
                'error': 'Por favor, especifica el modelo del vehiculo'})
        vehiculo.modelo = modelo
        vehiculo.save()
        return redirect('subastar_4', id=id)

    return render(request,
                  'users/subastar_step_3.html',
                  {'titulo': '¿Cuál es el modelo del vehículo?',
                   'id':id})

@login_required
def subastar_step_4(request,id):
    profile = Cuenta.objects.get(pk = request.user.pk)
    vehiculo = Vehiculo_Subasta.objects.filter(cuenta = profile).last()
    if request.method == 'POST': 
        try:
            vehiculo.año = request.POST['año']
            vehiculo.kilometraje = request.POST['kilometraje']
            if id != 2:
                vehiculo.motor = request.POST['motor']
                vehiculo.combustible = request.POST['combustible']
                if id == 1:
                    vehiculo.transmision = request.POST['transmision']
            else: 
                vehiculo.cilindraje = request.POST['cilindraje']
            vehiculo.placa = request.POST['placa']
            vehiculo.color = request.POST['color']
            vehiculo.estado_motor = request.POST['estado-motor']
            vehiculo.estado_chasis = request.POST['estado-chasis']
            vehiculo.estado_luces = request.POST['estado-luces']
            vehiculo.estado_llantas = request.POST['estado-llantas']
            especificaciones = request.POST['otras_especifi']
            
            if especificaciones != '':
                vehiculo.especificaciones = especificaciones

            vehiculo.save()
            
            return redirect('subastar_5', id=id)

        except:
            return render(request,
                'users/subastar_step_4.html',
                {'titulo': 'Más información del vehículo',
                'id':id,
                'error':'Es necesario llenar todos los espacios'})

    return render(request,
                  'users/subastar_step_4.html',
                  {'titulo': 'Más información del vehículo',
                   'id':id})

@login_required
def subastar_step_5(request,id):
    profile = Cuenta.objects.get(pk = request.user.pk)
    vehiculo = Vehiculo_Subasta.objects.filter(cuenta = profile).last()
    if request.method == 'POST':
        vehiculo.soat = request.POST['soat']
        if vehiculo.soat == 'Sí':
            try:
                vehiculo.fecha_soat = request.POST['soat_date']
            except:
                return render(request,
                  'users/subastar_step_5.html',
                  {'titulo': 'Más información del vehículo',
                   'id':id,
                   'error': 'Debe llenar todos los espacios'})
        vehiculo.tecno = request.POST['tecno']
        if vehiculo.tecno == 'Sí':
            try:
                vehiculo.fecha_tecno = request.POST['tecno_date']
            except:
                return render(request,
                    'users/subastar_step_5.html',
                    {'titulo': 'Más información del vehículo',
                    'id':id,
                    'error': 'Debe llenar todos los espacios'})    
        propietario = request.POST['propietario']
        if propietario == 'No':
            try:
                vehiculo.propietario = request.POST['name-prop-info']
                vehiculo.cc_propietario = request.POST['cc-prop-info']
                vehiculo.phone_propietario = request.POST['cel-prop-info']
            except:
                return render(request,
                  'users/subastar_step_5.html',
                  {'titulo': 'Más información del vehículo',
                   'id':id,
                   'error': 'Debe llenar todos los espacios'})
        else:
            vehiculo.propietario = request.user.first_name
        
        vehiculo.save()
        return redirect('subastar_6', id=id)

    return render(request,
                  'users/subastar_step_5.html',
                  {'titulo': 'Más información del vehículo',
                   'id':id})

@login_required
def subastar_step_6(request,id):
    profile = Cuenta.objects.get(pk = request.user.pk)
    vehiculo = Vehiculo_Subasta.objects.filter(cuenta = profile).last()
    return render(request,
                  'users/subastar_step_6.html',
                  {'titulo': 'Sube fotos del vehículo',
                   'id':id})
