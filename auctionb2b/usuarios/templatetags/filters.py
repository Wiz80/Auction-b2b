from django import template

register = template.Library()

@register.filter(name='get_municipios')
def get_municipios(datos_dane, departamento):
    return sorted(set(list(datos_dane['DEPARTAMENTO']==departamento)))