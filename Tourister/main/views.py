from django.shortcuts import render
from django. http import HttpRequest, HttpResponse
# Create your views here.

def home (request: HttpRequest):


    
    return render (request, "main/home.html" )


def abha (request: HttpRequest):


    
    return render (request, "main/Abha.html" )



def alula (request: HttpRequest):


    
    return render (request, "main/AlUla.html" )


def mekkah (request: HttpRequest):


    
    return render (request, "main/Mekkah.html" )

    

def riyadh (request: HttpRequest):


    
    return render (request, "main/Riyadh.html" )

