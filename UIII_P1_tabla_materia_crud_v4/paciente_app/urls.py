from django.urls import path
from paciente_app import views
urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarPaciente/", views.registrarPaciente, name="registrarPaciente" ),
    path("seleccionarPaciente/<codigo>", views.seleccionarPaciente, name="seleccionarPaciente"),
    path("editarPaciente/", views.editarPaciente, name="editarPaciente"),
    path("borrarPaciente/<codigo>", views.borrarPaciente, name="borrarPaciente")
    
]
