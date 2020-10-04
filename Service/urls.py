
from django.contrib import admin
from django.urls import path
from .views import home, knn_service

# esta es la parte de las URL
# esta es la lista de urls q va a tener tu projecto en django
# o en lo q sea xq al final todos lo tienen
# path( url, el metodo q responde a esa urls )
urlpatterns = [
    path('home/', home ),
    path('service/', knn_service)
]
