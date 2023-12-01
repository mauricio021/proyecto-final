from django.urls import path
from django.http import HttpResponse
from AppCoder.views import cursos_view , inicio_view, otra_view


urlpatterns = [
    path("inicio/", inicio_view),
    path("cursos/", cursos_view),
    path("otro/", otra_view)
]
