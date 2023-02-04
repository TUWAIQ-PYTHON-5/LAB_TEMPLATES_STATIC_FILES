from django.urls import path
from . import views

app_name = "TouristesrAreas"

urlpatterns = [
    path("", views.Home_page, name="Home_page"),
    path("Riyadh/", views.Riyadh_page, name="Riyadh_page"),
    path("Abha/", views.Abha_page, name="Abha_page"),
    path("Mekkah/", views.Mekkah_page, name="Mekkah_page"),
    path("AlUla/", views.AlUla_page, name="AlUla_page"),
]