from AppCoder.views import *
from django.urls import path

urlpatterns = [
    path('curso/', curso),
    path('paguina-inicio/', inicio),
    path('profesores/', profesor),
    path('estudiantes/', estudiante),
    path('entregables/', entregable),
]
