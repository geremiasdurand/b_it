from django.db import models

# Create your models here.
#Modelo de Usuario utilizado para la DB
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25, null=True)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=80)
    es_arrendador = models.BooleanField(default=False)
