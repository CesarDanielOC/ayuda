from django.db import models

# Create your models here.
class Paciente(models.Model):
    codigo= models.CharField(primary_key=True, max_length=6)
    nombre= models.CharField(max_length=100)
    creditos=models.CharField(max_length=60)
    apellido=models.CharField(max_length=30)
    fechanacimiento=models.DateField()
    telefono=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    fecharegistro=models.DateField()

    def __str__(self):
        return self.nombre