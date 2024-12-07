from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse("Bienvenidos a Examen Parcial")

def vistaPrincipal(request):
    nombre = "Nelson en vista princial"
    return render(request,'vistaPrincipal.html',{
        'nombre':nombre
    })

def crearArtiulo(request):
    nombre = "Creando articulo"
    return render(request,'crearArtiulo.html')

def crearTema(request):
    nombre = "Crear Tema"
    return render(request,'crearTema.html')

def verArticulo(request):
    nombre = "ver Articulo"
    return render(request,'verArticulo.html')

def buscarArticulo(request):
    nombre = "Buscar Articulo"
    return render(request,'buscarArticulo.html')
