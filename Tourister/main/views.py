from django.shortcuts import render,resolve_url
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home_page(request:HttpRequest):


    return render(request ,'main/base.html'  )


def riyadh_page(request:HttpRequest):

    return render(request ,'main/Riyadh.html' )   


def abha_page(request :HttpRequest):

    return render(request , 'main/Abha.html' )   

def makkah_page(request : HttpRequest):
    
    return render(request,'main/Mekkah.html')  

def Alula(request :HttpRequest):
    return render(request , 'main/AlUla.html')