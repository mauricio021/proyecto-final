from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context



def inicio_view(xx):
    return HttpResponse ("Bienvenidoo")

def v_cursos_view(xx):           #   ESTA ES LA VIEW CURSOS VIEJA
    #return HttpResponse ("Aca te muestro mis cursossss")
    return render(xx, "AppCoder/padre.html")

def cursos_view(xx):
    nombre = "Mariano Cristian"
    apellido = "Orozco"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "ciudades": ["Buenos Aires", "Cordoba"]
    }                 # Para enviar al contexto


    ruta = "C:\\Users\\maubs\\ProyectoFinal\\ProyectoFinal2\\AppCoder\\templates\\AppCoder\\padre.html"
    mi_archivo = open(ruta, "r")

    # Metodo django (+ complicado)
    plantilla = Template(mi_archivo.read())   #  Carga el template 
    contexto = Context(diccionario)  # Le doy al contexto mi nombre y apellido
    documento = plantilla.render(contexto)   #  Renderizamos(cargamos) en el documento la plantilla

    return HttpResponse(documento)


def otra_view(xx):
    nombre = "Mariano Cristian"
    apellido = "Orozco"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
    }  

#   Segundo metodo django (+ sencillo)
    return render(xx, "AppCoder/padre.html", diccionario) 



