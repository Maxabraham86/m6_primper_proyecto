from django.urls import path 
from ejemplos.views import *

urlpatterns =[
    path('', hola),
    path('chao/', chao),
    path('saludar/<nombre>', saludar),
    path('poliglota/<nombre>/<idioma>', poliglota),
    path('mascotas/', mascota)
]


