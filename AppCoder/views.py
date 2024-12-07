
from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso, Profesor, Entregable, Estudiante

def curso(request):
    curso = Curso.objects.all() #Esto se obtienen los atributos completos de la clase
    print(curso)
    
    return render(request, 'AppCoder/cursos.html', {'cursos':curso})#Es el renderizado para las templates de la seccion Curso

def inicio(request):
    return render(request, 'AppCoder/index.html') #Es el renderizado para las templates de la seccion Inicio

def profesor(request):
    profesor = Profesor.objects.all() #Esto se obtienen los atributos completos de la clase
    print(profesor)
    
    return render(request, 'AppCoder/profesores.html', {'profesor':profesor}) #Es el renderizado para las templates de la seccion profesores

def estudiante(request):
    estudiante = Estudiante.objects.all() #Esto se obtienen los atributos completos de la clase
    print(estudiante)
    
    return render(request, 'AppCoder/estudiantes.html', {'estudiante':estudiante}) #Es el renderizado para las templates de la seccion estudiantes

def entregable(request):    
    entregable = Entregable.objects.all() #Esto se obtienen los atributos completos de la clase
    print(entregable)
    
    return render(request, 'AppCoder/entregables.html', {'entregable':entregable}) #Es el renderizado para las templates de la seccion entregables