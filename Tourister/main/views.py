from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def base_page(request : HttpRequest):
   
    return render(request , "main/base.html")



def riyadh_page(request : HttpRequest):
   
    return render(request , "main/riyadh.html")

def abha_page(request : HttpRequest):
   
    return render(request , "main/abha.html")

def mekkah_page(request : HttpRequest):
   
    return render(request , "main/mekkah.html")

def alula_page(request : HttpRequest):
   
    return render(request , "main/alula.html")