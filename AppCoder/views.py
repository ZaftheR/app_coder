
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Curso, Profesor, Entregable, Estudiante
from .forms import CursoFormulario, EstudiantesFormulario, ProfesoresFormulario, EntregablesFormulario

def curso(request):
    
    query = request.GET.get('q')
    if query:
        curso =  Curso.objects.filter(nombre__icontains=query) | Curso.objects.filter(comision__icontains=query)
    else:
        curso = Curso.objects.all() #Esto se obtienen los atributos completos de la clase
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


def formulario_curso_api(request):
    
    if request.method == "POST":
        curso_form = CursoFormulario(request.POST)
        
        if curso_form.is_valid():
            info_limpia = curso_form.cleaned_data
            curso = Curso(nombre=info_limpia["nombre"], comision=info_limpia["comision"])
            curso.save()
            return redirect("cursos")
    else:
        curso_form = CursoFormulario()
    
    contexto = {"curso_form": curso_form}
    
    return render(request, 'AppCoder/forms/curso-formulario.html', contexto)

def formulario_estudiantes_api(request):
    
    if request.method == "POST":
        estudiantes_form = EstudiantesFormulario(request.POST)
        
        if estudiantes_form.is_valid():
            info_limpia = estudiantes_form.cleaned_data
            estudiantes = Estudiante(nombre=info_limpia["nombre"], apellido=info_limpia["apellido"], email=info_limpia["email"])
            estudiantes.save()
            return redirect("estudiantes-formulario")
    else:
        estudiantes_form = EstudiantesFormulario()
    
    contexto = {"estudiantes_form": estudiantes_form}
    
    return render(request, 'AppCoder/forms/estudiante-formulario.html', contexto)


def formulario_profesores_api(request):
    
    if request.method == "POST":
        profesores_form = ProfesoresFormulario(request.POST)
        
        if profesores_form.is_valid():
            info_limpia = profesores_form.cleaned_data
            profesor = Profesor(nombre=info_limpia["nombre"], apellido=info_limpia["apellido"], email=info_limpia["email"], profesion=info_limpia["profesion"])
            profesor.save()
            return redirect("profesores")
    else:
        profesores_form = ProfesoresFormulario()
    
    contexto = {"profesores_form": profesores_form}
    
    return render(request, 'AppCoder/forms/profesores-formulario.html', contexto)


def formulario_entregrables_api(request):
    
    if request.method == "POST":
        entregables_form = EntregablesFormulario(request.POST)
        
        if entregables_form.is_valid():
            info_limpia = entregables_form.cleaned_data
            entregables = Entregable(nombre=info_limpia["nombre"], fechaDeEntrega=info_limpia["fecha de Entrega"], entregado=info_limpia["entregado"])
            entregables.save()
            return redirect("entregables")
    else:
        entregables_form = EntregablesFormulario()
    
    contexto = {"entregables_form": entregables_form}
    
    return render(request, 'AppCoder/forms/entregables-formulario.html', contexto)



