from django.urls import path
from ejercicios_ruteo.views import root, index, new, create, show, edit, destroy , yeison


urlpatterns =[
    path('',root),
    path('blogs/', index),
    path('blogs/new', new),
    path('blogs/create', create),
    path('blogs/json', yeison),
    path('blogs/<number>', show),
    path('blogs/<number>/edit', edit),
    path('blogs/<number>/delete', destroy),
    
    
]
