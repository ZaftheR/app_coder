from django.db import models
"""agregar mas detalles a los cursos y a las demas clases como horarios, fechas, mas datos en otras clases"""
class Curso(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    comision = models.IntegerField()  # Campo entero
    
    def __str__(self):
        return f'Nombre del curso: {self.nombre} | comision: {self.comision}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 100 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 100 caracteres
    email = models.EmailField()  # Campo de email
    
    def __str__(self):
        return f'Estudiante: {self.apellido}, {self.nombre} | e-mail: {self.email}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 30 caracteres
    email = models.EmailField()  # Campo de email
    profesion = models.CharField(max_length=50)  # Campo string de 50 caracteres
    
    def __str__(self):
        return f"Profesor: {self.apellido}, {self.nombre} | Curso: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    fechaDeEntrega = models.DateField()  # Campo de fecha
    entregado = models.BooleanField()  # Campo booleano
    
    def __str__(self):
        return f"Alumno: {self.nombre} | Fecha de entrega: {self.fechaDeEntrega} | Entregado: {self.entregado}"

