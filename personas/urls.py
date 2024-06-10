from django.urls import path
from personas.views import  home, exito



urlpatterns =[
    path('',home),
    path('exito/',exito),
    
    
]
