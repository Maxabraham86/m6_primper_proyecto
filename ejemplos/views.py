from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hola(req):
    return HttpResponse('Hola curso!')

def chao(req):
    return HttpResponse('Chao Pescao!')

def saludar(req, nombre):
    return HttpResponse(f'<h1> Hola {nombre}</h1>')

def poliglota(req, nombre, idioma):
#    "saluda a la persona dependiendo del idioma ingresado"

    if idioma == 'ingles':
        return HttpResponse(f'Hello {nombre}')
    elif idioma == 'arabe':
        return HttpResponse(f'Salam Alaykum {nombre}')
    elif idioma == 'portugues':
        return HttpResponse(f'Hoi {nombre}')
    else:
        return HttpResponse ('No entiendo ese idioma')

def mascota(req):
    return HttpResponse(
        '''
        <h1> Mascotapp</h1>
        <p> Mascotas para ti </p>
        <img src="https://picsum.photos/1000/800">
        '''
    )



