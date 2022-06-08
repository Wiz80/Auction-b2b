from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
#from django.core.files import File  # you need this somewhere
#import urllib
#import os


# Create your models here.
class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name = 'Fecha_Nacimiento')
    cc = models.IntegerField(verbose_name='cc')
    departamento = models.CharField(max_length = 80, verbose_name="Departamento")
    ciudad = models.CharField(max_length = 80, verbose_name="Ciudad")
    phone = models.IntegerField(verbose_name="Phone")
    slug = models.CharField(unique = True, max_length=150, verbose_name="URL", null = True)
    picture = models.ImageField(upload_to = 'usuarios/pictures', blank=True, null = True)

    class Meta:
        verbose_name = "Cuenta"
    
    def __str__(self):
        return self.user.username
    

class Vehiculo_Subasta(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT)
    categoria = models.CharField(max_length = 20, verbose_name = "categoria", null = True)
    marca = models.CharField(max_length = 20, verbose_name = "marca", null = True)
    modelo = models.CharField(max_length = 20, verbose_name = "modelo", null = True)
    año = models.IntegerField(verbose_name = "año", null = True)
    kilometraje = models.IntegerField(verbose_name = "kilometraje", null = True)
    motor = models.CharField(max_length = 20, verbose_name = "motor", null = True, blank = True)
    cilindraje = models.CharField(max_length = 20, verbose_name = "cilindraje", null = True, blank = True)
    combustible = models.CharField(max_length = 20, verbose_name = "combustible", null = True)
    placa = models.CharField(max_length = 6, verbose_name = "placa", null = True)
    color = models.CharField(max_length = 20, verbose_name = "color", null = True)
    estado_motor = models.IntegerField(verbose_name="estado-motor", null = True)
    estado_chasis = models.IntegerField(verbose_name="estado-chasis", null = True)
    estado_luces = models.IntegerField(verbose_name="estado-luces", null = True)
    estado_llantas = models.IntegerField(verbose_name="estado-motor", null = True)
    especific_estado = models.CharField(max_length = 200, verbose_name="especific-estado", null = True)
    soat = models.CharField(max_length = 2, verbose_name = "soat")
    fecha_soat = models.CharField(max_length = 20, verbose_name = "fecha_soat", blank = True, null = True)
    tecno = models.CharField(max_length = 2, verbose_name = "tecno", null = True)
    fecha_tecno = models.CharField(max_length = 20, verbose_name = "fecha tecnomecánica", null = True)
    propietario_es = models.CharField(max_length = 2, verbose_name = "propietario_es", null = True, blank = True)
    propietario = models.CharField(max_length = 100, verbose_name = "propietario", null = True, blank = True)
    cc_propietario =  models.IntegerField(verbose_name = "cc-propietario", null = True, blank = True)
    phone_propietario = models.CharField(max_length = 10, verbose_name = "phone_propietario", null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Info Vehiculo"
    
    def __str__(self):
        return self.modelo
    
class Foto_Vehiculo(models.Model):
    def get_upload_to(instance, filename):
        return 'usuarios/%s/%s/%s' % (instance.cuenta, instance.vehiculo.modelo ,filename)
    
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, max_length=10)
    vehiculo = models.ForeignKey(Vehiculo_Subasta, on_delete=models.CASCADE, max_length=10)
    photo = models.ImageField(upload_to=get_upload_to, blank=True)
    name = models.CharField(max_length=100, null = True)

    class Meta:
        verbose_name = "Foto Vehiculo"
    
    def __str__(self):
        return self.vehiculo.modelo
    
class Info_Subasta(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, max_length=10)
    vehiculo = models.ForeignKey(Vehiculo_Subasta, on_delete=models.CASCADE, max_length=10)
    tipo_subasta = models.CharField(max_length=2, null=True)
    precio = models.CharField(max_length = 50, null= True)
    departamento = models.CharField(max_length = 50, null= True)
    municipio = models.CharField(max_length = 50, null= True)
    fecha_inicio = models.DateTimeField(auto_now_add=False, null = True)
    fecha_cierre = models.DateTimeField(auto_now_add=False, null = True)

    class Meta:
        verbose_name = "Info Subasta"
    
    def __str__(self):
        return self.cuenta.user.username
    