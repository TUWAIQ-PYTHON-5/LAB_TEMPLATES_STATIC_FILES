from django.shortcuts import render, resolve_url
from django.http import HttpRequest, HttpResponse

# Create your views here.

#first page
def home_page(request : HttpRequest):
    return render(request, "main/home.html")

#second page
def Aola_city(request : HttpRequest):
    return render(request, "main/Alola.html")

#therd page
def Albaha_city(request : HttpRequest):
    return render(request, "main/Albaha.html")

#fourth page
def Makkah_city(request : HttpRequest):
    return render(request, "main/Makkah.html")

#fifth page
def Tabuk_city(request : HttpRequest):
    return render(request, "main/Tabuk.html")


