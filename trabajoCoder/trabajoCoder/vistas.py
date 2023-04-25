from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo= "Bienvenido, usuario!"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Bienvenido, usuario! Fecha: {hoy.day}/{hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html