from django.urls import path
from . import views

app_name = "main"

urlpatterns= [
    path('', views.Home, name="home_page"),
    path("city/Riyadh/", views.Riyadh, name="Riyadh_page"),
    path("city/Qassim/", views.Qassim, name="Qassim_page"),
    path("city/Mekkah/", views.Mekkah, name="Mekkah_page"),
    path("city/AlUla/", views.AlUla, name="AlUla_page"),

]
