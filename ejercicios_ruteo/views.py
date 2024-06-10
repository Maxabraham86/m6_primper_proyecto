from django.shortcuts import render, redirect
from django.http import HttpResponse ,JsonResponse
# Create your views here.

def root(req):
    return redirect('/blogs')

def index(req):
    return render(req, 'blogs.html')
#('placeholder para luego mostrar una lista de todos los blogs')

def new(req):
    return HttpResponse ('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def create (req):
    return redirect ('/')

def show(req,number ):
    
    return HttpResponse(f'placeholder para mostrar el blog número: {number}')

def edit (req, number):
    return HttpResponse (f'placeholder para editar el blog {number}')

def destroy(req,number):
    return redirect('/blogs')

def yeison(req):
    return JsonResponse({
        'blog1': 'un blog para viajeros',
        'blog2': ' un blog de cocina',
        'blog3': ' un blog de viajeros que cosinan'
    })
