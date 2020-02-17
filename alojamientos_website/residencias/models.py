from django.db import models
from register.models import Usuario

# Create your models here.
#Modelo de Departamentos utilizado para la DB
class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

#Modelo de Residencias utilizado para la DB
class Residencia(models.Model):
    id = models.AutoField(primary_key=True)
    id_arrendador = models.ForeignKey("register.Usuario", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    direccion_principal = models.CharField(max_length=50)
    direccion_secundaria = models.CharField(max_length=50)
    id_departamento = models.ForeignKey("Departamento", on_delete=models.CASCADE)
    barrio = models.CharField(max_length=25)
    cantidad_de_lugarares = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.TextField()
