from django.shortcuts import render, redirect
from django.http import HttpResponse
from personas.forms import PersonaForm
from personas.models import Persona

# Create your views here.
def home(req):
    if req.method == 'GET':
        form = PersonaForm()
        context={'form':form}
        return render(req, 'personas.html', context)
    else:
        #validar el formulario
        form = PersonaForm(req.POST)
        if form.is_valid():
            Persona.objects.create(
            #esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario    
                **form.cleaned_data
            )
            return redirect('/personas/exito/')
        context ={'form':form}
        
    return render(req, 'personas.html', context)


def exito (req):
    return HttpResponse ('Eeeexito!!!')