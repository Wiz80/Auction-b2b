from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Cuenta, Foto_Vehiculo, Info_Subasta, Vehiculo_Subasta
# Register your models here.

@admin.register(Info_Subasta)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('tipo_subasta','cuenta','vehiculo','precio')

@admin.register(Foto_Vehiculo)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('cuenta','vehiculo','photo')

@admin.register(Vehiculo_Subasta)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('cuenta','categoria','marca', 'año')

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('pk','user','picture', 'phone')
    list_display_links = ('pk', 'user')
    #list_editable = ()
    search_fields = (
        'user__username',
        'user__email', 
        'user__first_name', 
        'user__last_name',
        'phone')

    fieldsets = (
    ('Cuenta', {
            'fields':(('user', 'picture'),),
        }),
    ('Extra info',{
        'fields':(
            ('phone', 'birth_date', 'cc'),
            ('departamento', 'ciudad')
        )
    }),
    )

class CuentaInline(admin.StackedInline):
    model = Cuenta
    can_delete = False
    verbose_name_plural = 'Cuentas'

class VehiculoInline(admin.StackedInline):
    model = Vehiculo_Subasta
    can_delete = False
    verbose_name_plural = "Vehiculos"

class FotoInline(admin.StackedInline):
    model = Foto_Vehiculo
    can_delete = False
    verbose_name_plural = "Fotos"

class InfoInline(admin.StackedInline):
    model = Info_Subasta
    can_delete = False
    verbose_name_plural = "Subastas"




class UserAdmin(BaseUserAdmin):
    inlines = (CuentaInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

title = "Auction B2B"
subtitle = "Gestión DB"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle