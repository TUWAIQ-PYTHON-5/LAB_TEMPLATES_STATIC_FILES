from django.shortcuts import render,resolve_url
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_page(request:HttpRequest):
    return render(request,"main/base.html")

def riyadh_page(request:HttpRequest):
    return render(request,"main/riyadh.html")

def abha_page(request:HttpRequest):
    return render(request,"main/abha.html")

def mekkah_page(request:HttpRequest):
    return render(request,"main/makkah.html")

def alula_page(request:HttpRequest):
    return render(request,"main/alula.html")
    
