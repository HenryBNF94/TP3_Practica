from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# Vista para la página de inicio
def hola(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())

#  Vista para la página de ofertas
def ofertas(request):
    template = loader.get_template('ofertas.html')
    return HttpResponse(template.render())

# Vista para la página de productos
def productos(request):
    template = loader.get_template('productos.html')
    return HttpResponse(template.render())

# Vista para la página de servicios
def servicios(request):
    template = loader.get_template('servicios.html')
    return HttpResponse(template.render())

# Vista para la página de contacto
def contacto(request):
    template = loader.get_template('contacto.html')
    return HttpResponse(template.render())