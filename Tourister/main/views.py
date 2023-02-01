from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.


def Home (request : HttpRequest):
    context = {
    }

    return render(request ,"main/home.html",context)


def Riyadh (request : HttpRequest):
    context = {
    }

    return render(request ,"main/Riyadh.html",context)


def Qassim (request : HttpRequest):
    context = {
    }

    return render(request ,"main/Qassim.html",context)


def Mekkah (request : HttpRequest):
    context = {
    }

    return render(request ,"main/Mekkah.html",context)

def AlUla (request : HttpRequest):
    context = {
    }

    return render(request ,"main/AlUla.html",context)