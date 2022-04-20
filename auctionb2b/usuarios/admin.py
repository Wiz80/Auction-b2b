from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Cuenta
# Register your models here.

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

class UserAdmin(BaseUserAdmin):
    inlines = (CuentaInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

title = "Auction B2B"
subtitle = "Gestión DB"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle