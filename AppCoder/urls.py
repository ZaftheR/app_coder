from AppCoder.views import curso, entregable, estudiante, inicio, profesor, formulario_curso_api, formulario_estudiantes_api, formulario_profesores_api, formulario_entregrables_api
from django.urls import path

urlpatterns = [
    path('curso/', curso, name='cursos'),
    path('', inicio, name= 'inicio'),
    path('profesores/', profesor, name= 'profesores'),
    path('estudiantes/', estudiante, name= 'estudiantes'),
    path('entregables/', entregable, name= 'entregables'),
    path('curso-formulario/', formulario_curso_api, name= 'curso-formulario'),
    path('estudiantes-formulario/', formulario_estudiantes_api, name= 'estudiantes-formulario'),
    path('profesores-formulario/', formulario_profesores_api, name= 'profesores-formulario'),
    path('entregables-formulario/', formulario_entregrables_api, name= 'entregables-formulario'),
    
]
