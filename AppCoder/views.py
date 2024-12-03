from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

def curso(request):
    return render(request, 'AppCoder/cursos.html')
def inicio(request):
    return render(request, 'AppCoder/index.html')

def profesor(request):
    return HttpResponse('Vista de profesores')

def estudiante(request):
    return HttpResponse('Vista de alumnos')

def entregable(request):
    return HttpResponse('Vista de entregables')