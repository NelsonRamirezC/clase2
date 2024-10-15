from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    contexto = {
        "titulo": "Bienvenidos a nuestra web",
    }
    return render(request, 'home.html', contexto)

def contacto(request):
    contexto = {
        "titulo": "Gracias por querer contactarte con nosotros"
    }
    return render(request, 'contacto.html', contexto)

def reclamos(request):
    contexto = {
        "titulo": "Deja tu reclamo en el siguiente Formulario"
    }
    return render(request, 'reclamos.html', contexto)
