from django.shortcuts import render , resolve_url
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request : HttpRequest):

    return render(request , "main/home.html" )



def riyadh(request : HttpRequest):
    riyadh_url = resolve_url("main:riyadh")
    return render(request , "main/riyadh.html" )




def almaa(request : HttpRequest):

    return render(request , "main/almaa.html" )





