from django.db import models

# Create your models here.
class Animal (models.Model):
    especie      = models.CharField(max_length=64)
    nombre       = models.CharField(max_length=64)
    descripcion  = models.CharField(max_length=500)
    imagen       = models.ImageField(upload_to='images')
    tamaño       = models.CharField(max_length=32)
    apto_niños   = models.BooleanField()

class Establecimiento (models.Model):
    nombre      = models.CharField(max_length=64)
    direccion   = models.CharField(max_length=255)
    horario     = models.CharField(max_length=64)
    imagen      = models.ImageField(upload_to='images')
    descripcion = models.CharField(max_length=500)
    pagina_web  = models.CharField(max_length=255)

class Producto (models.Model):
    nombre           = models.CharField(max_length=64)
    descripcion      = models.CharField(max_length=500)
    imagen           = models.ImageField(upload_to='images')
    especie_objetivo = models.CharField(max_length=255)
    tipo             = models.CharField(max_length=32)
