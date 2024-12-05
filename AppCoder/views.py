
from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso

def curso(request):
    curso = Curso.objects.all()
    print(curso)
    
    return render(request, 'AppCoder/cursos.html') #Es el renderizado para las templates de la seccion Curso

def inicio(request):
    return render(request, 'AppCoder/index.html') #Es el renderizado para las templates de la seccion Inicio

def profesor(request):
    return render(request, 'AppCoder/profesores.html') #Es el renderizado para las templates de la seccion profesores

def estudiante(request):
    return render(request, 'AppCoder/estudiantes.html') #Es el renderizado para las templates de la seccion estudiantes

def entregable(request):
    return render(request, 'AppCoder/entregables.html') #Es el renderizado para las templates de la seccion entregables