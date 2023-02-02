from django.shortcuts import render, resolve_url
from django.http import HttpRequest, HttpResponse

def home_page(request : HttpRequest) :
   return render(request, "main/homepage.html")


def about(request : HttpRequest) :
    return render(request, "main/about.html")

def contact(request : HttpRequest) :
    return render(request, "main/contact.html")

def riyadh_page(request : HttpRequest) :
    return render(request, "main/riyadh.html")

def abha_page(request : HttpRequest) :
    return render(request, "main/abha.html")

def mekkah_page(request : HttpRequest) :
    return render(request, "main/mekkah.html")

def alula_page(request : HttpRequest) :
    return render(request, "main/alula.html")