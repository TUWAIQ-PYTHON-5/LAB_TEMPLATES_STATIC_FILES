from django.shortcuts import render 
from django.http import HttpRequest,HttpResponse
# Create your views here.


def home(request):
    return render(request,'cities/home.html')

def riyadh(request):
    return render(request,'cities/riyadh.html')

def abha(request):
    return render(request,'cities/abha.html')

def mekkah(request):
    return render(request,'cities/mekkah.html')

def alula(request):
    return render(request,'cities/alula.html')