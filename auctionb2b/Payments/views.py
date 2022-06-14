from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def comprar_creditos(request):
    return render(request, 'pagos\comprar_creditos.html')
