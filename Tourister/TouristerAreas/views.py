from django.shortcuts import render, resolve_url
from django.http import HttpRequest, HttpResponse


# Create your views here.
def Home_page(request : HttpRequest):
    
    return render(request, "TouristerAreas/Home.html")


def Abha_page(request : HttpRequest):

    
    return render(request, "TouristerAreas/Abha.html")


def Riyadh_page(request : HttpRequest):
    
    return render(request, "TouristerAreas/Riyadh.html")

def Mekkah_page(request : HttpRequest):

    return render(request, "TouristerAreas/Mekkah.html")

def AlUla_page(request : HttpRequest):
    
    return render(request, "TouristerAreas/AlUla.html")