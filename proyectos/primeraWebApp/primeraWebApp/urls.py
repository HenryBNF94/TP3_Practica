"""
URL configuration for primeraWebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hola, name='inicio'), # Ruta para la página de inicio
    path('ofertas/', ofertas, name='ofertas'), # Ruta para la página de ofertas
    path('productos/', productos, name='productos'),  # Ruta para la página de productos
    path('servicios/', servicios, name='servicios'),  # Ruta para la página de servicios
    path('contacto/', contacto, name='contacto'),  # Ruta para la página de contacto
]
