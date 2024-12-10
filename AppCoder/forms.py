from django import forms 

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()