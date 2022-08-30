from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=15)
    edad= models.IntegerField()
    generos = [('m', 'masculino'), ('f', 'femenino')]
    sexo= models.CharField(max_length=1,choices=generos)
    fecha_de_nacimiento = models.DateField()
