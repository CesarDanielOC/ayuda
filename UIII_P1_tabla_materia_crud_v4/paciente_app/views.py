from django.shortcuts import render, redirect
from .models import Paciente

# Create your views here.
def inicio_vista(request):
    lospacientes= Paciente.objects.all()
    return render(request, "gestionarPaciente.html", {"mispacientes":lospacientes}) 

def registrarPaciente (request):
    codigo= request.POST["txtcodigo"]
    nombre= request.POST["txtnombre"]
    creditos= request.POST["numcreditos"]
    apellido= request.POST["txtapellido"]
    fechanacimiento= request.POST["txtfechanacimiento"]
    telefono= request.POST["txttelefono"]
    direccion= request.POST["txtdireccion"]
    fecharegistro= request.POST["txtfecharegistro"]


    guardarpaciente=Paciente.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos, apellido=apellido,  fechanacimiento=fechanacimiento, telefono=telefono, direccion=direccion, fecharegistro=fecharegistro
    )   # GUARDA EL REGISTRO 

    return redirect("/")

def seleccionarPaciente(request, codigo):
    paciente=Paciente.objects.get(codigo=codigo)
    return render(request, "editarpaciente.html", {"mispacientes": paciente})



def editarPaciente(request):
        codigo= request.POST["txtcodigo"]
        nombre= request.POST["txtnombre"]
        creditos= request.POST["numcreditos"]
        apellido=request.POST["txtapellido"]
        fechanacimiento= request.POST["txtfechanacimiento"]
        telefono= request.POST["txttelefono"]
        direccion= request.POST["txtdireccion"]
        fecharegistro= request.POST["txtfecharegistro"]
        paciente=Paciente.objects.get(codigo=codigo)
        paciente.nombre=nombre
        paciente.creditos=creditos
        paciente.apellido=apellido
        paciente.fechanacimiento=fechanacimiento
        paciente.telefono=telefono
        paciente.direccion=direccion
        paciente.fecharegistro=fecharegistro
        paciente.save() #guardar registro actualizado 
        return redirect("/")

def borrarPaciente(request, codigo):
    paciente=Paciente.objects.get(codigo=codigo)
    paciente.delete() #borra el registro
    return redirect("/")