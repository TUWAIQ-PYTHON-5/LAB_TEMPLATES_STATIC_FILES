
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request : HttpRequest):
   
    return render(request , "main/home.html")


def riyadh_page(request : HttpRequest):
   
    return render(request , "main/riyadh.html")

def abha_page(request : HttpRequest):
   
    return render(request , "main/abha.html")

def makkah_page(request : HttpRequest):
   
    return render(request , "main/makkah.html")

def alula_page(request : HttpRequest):
   
    return render(request , "main/alula.html")