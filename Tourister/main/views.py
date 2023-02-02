from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_bage(request: HttpRequest):
    
    return render(request, "main/home.html")

def arar_city(request: HttpRequest):
    
    return render(request, "main/arar.html")

def abha_city(request: HttpRequest):
    
    return render(request, "main/abha.html")


def riyadh_city(request: HttpRequest):
    
    return render(request, "main/riyadh.html")


def alula_city(request: HttpRequest):

    return render(request, "main/alula.html")




