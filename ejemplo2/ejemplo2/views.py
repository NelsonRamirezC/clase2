from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    contexto = {}
    return render(request, 'home.html', contexto)

def contacto(request):
    contexto = {}
    return render(request, 'contacto.html', contexto)

def reclamos(request):
    contexto = {}
    return render(request, 'reclamos.html', contexto)
