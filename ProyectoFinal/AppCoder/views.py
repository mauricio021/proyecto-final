from django.shortcuts import render
from django.http import HttpResponse


def inicio_view(xx):
    return HttpResponse ("Bienvenidoo")

def cursos_view(xx):
    #return HttpResponse ("Aca te muestro mis cursossss")
    return render(xx, "AppCoder/padre.html")
