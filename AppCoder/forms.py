from django import forms 

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()
    
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)  # Campo string de 100 caracteres
    apellido = forms.CharField(max_length=30)  # Campo string de 100 caracteres
    email = forms.EmailField()
    
class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)  # Campo string de 30 caracteres
    apellido = forms.CharField(max_length=30)  # Campo string de 30 caracteres
    email = forms.EmailField()  # Campo de email
    profesion = forms.CharField(max_length=50)  # Campo string de 50 caracteres
    
class EntregablesFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)  # Campo string de 100 caracteres
    fechaDeEntrega = forms.DateField()  # Campo de fecha
    entregado = forms.BooleanField()  # Campo booleano