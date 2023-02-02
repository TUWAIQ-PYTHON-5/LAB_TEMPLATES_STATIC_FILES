from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.\

def index(request : HttpRequest):


    return render(request, "main/index.html" )


def Riyadh_page(request : HttpRequest):


    return render(request, "main/Riyadh.html" )



def Abha_page(request : HttpRequest):


    return render(request, "main/Abha.html" )




def Makkah_page(request : HttpRequest):


    return render(request , "main/Mekkah.html")


def Alula_page(request : HttpRequest):


    return render(request , "main/Ola.html")