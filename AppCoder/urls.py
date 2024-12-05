from AppCoder.views import curso, entregable, estudiante, inicio, profesor
from django.urls import path

urlpatterns = [
    path('curso/', curso, name='cursos'),
    path('', inicio, name= 'inicio'),
    path('profesores/', profesor, name= 'profesores'),
    path('estudiantes/', estudiante, name= 'estudiantes'),
    path('entregables/', entregable, name= 'entregables'),
]
