
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Curso, Profesor, Entregable, Estudiante
from .forms import CursoFormulario

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


def fomulario_curso(request):
    
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"], comision=request.POST["comision"])
        curso.save()
        return redirect('cursos')
    else:
        return render(request, 'AppCoder/forms/curso-formulario.html')

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
