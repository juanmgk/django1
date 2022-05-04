from django.http import HttpResponse
import datetime

from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola!")

def segundaVista(request):
    return HttpResponse("Esta es mi segunda vista")

def diaHoy(request):
    dia = datetime.datetime.now()
    texto = f"Hoy es: {dia}"
    return HttpResponse(texto)

def miNombre(request, nombre):
    texto = f"Mi nombre es {nombre}"
    return HttpResponse(texto)

def edad(self, edad):
    edad2 = int(edad)
    anio = datetime.datetime.today().year
    anio2 = int(anio)
    nacimiento = anio2-edad2
    texto = f'Usted nació en el año {nacimiento}'
    return HttpResponse(texto)

def pruebaTemplate(request):
    miHtml = open("C:/Users/A309509/OneDrive - Santander Office 365/Documentos/Cursos/Coderhouse - Python/Proyecto2/Templates/template.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)