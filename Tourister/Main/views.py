from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def home_page(request : HttpRequest):
    return render(request,"Main/Home_Page.html")

def city_riyadh(request : HttpRequest):
    return render(request,"Main/riyadh.html")

def city_alula(request : HttpRequest):
    return render(request,"Main/alula.html")

def city_mekkah(request : HttpRequest):
    return render(request,"Main/mekkah.html")

def city_abha(request : HttpRequest):
    return render(request,"Main/abha.html")

