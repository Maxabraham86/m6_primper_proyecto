from django.urls import path
from mascotas.views import paginaMascotas, detalleMascotas, crear_mascota



urlpatterns =[
    path('',paginaMascotas),
    path('home/', paginaMascotas),
    path('<id>/', detalleMascotas),
    path('create/', crear_mascota)
]
