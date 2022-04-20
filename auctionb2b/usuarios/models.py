from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name = 'Fecha_Nacimiento')
    cc = models.IntegerField(verbose_name='cc')
    departamento = models.CharField(max_length = 80, verbose_name="Departamento")
    ciudad = models.CharField(max_length = 80, verbose_name="Ciudad")
    phone = models.IntegerField(verbose_name="Phone")
    slug = models.CharField(unique = True, max_length=150, verbose_name="URL")
    picture = models.ImageField(upload_to = 'usuarios/pictures', blank=True, null = True)

    class Meta:
        verbose_name = "Cuenta"

    def __str__(self):
        return self.user.username