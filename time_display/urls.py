from django.urls import path
from time_display.views import index


urlpatterns=[
    path('', index)
    
]