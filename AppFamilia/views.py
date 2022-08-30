from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from AppFamilia import models
from django.template import loader
from AppFamilia.models import Familiar

# Create your views here.

def mostrar_familia(request):
    mama = Familiar(nombre = "Marianela",edad= 45,sexo= "f", fecha_de_nacimiento='1976-11-22')
    mama.save()
    hermana = Familiar(nombre = "Melisa",edad= 6,sexo= "f", fecha_de_nacimiento='2005-07-05')
    hermana.save()
    abuela = Familiar(nombre = "Liliana",edad= 77,sexo= "f", fecha_de_nacimiento='1955-02-06')
    abuela.save()

    plantilla = loader.get_template('familias.html')
    familia = {'miembros': [mama,hermana,abuela]}
    documento = plantilla.render(familia)

    return HttpResponse(documento)