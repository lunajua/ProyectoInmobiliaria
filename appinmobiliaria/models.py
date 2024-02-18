from django.db import models

# Create your models here.

class Propiedad(models.Model):
    direccion = models.CharField(max_length=40)
    tipo_de_propiedad = models.CharField(max_length=40)
    localizacion = models.CharField(max_length=40)
    palabra_clave =models.CharField(max_length=40)
    metros = models.IntegerField()
    ambientes = models.IntegerField() 
    banos = models.IntegerField()
    descripcion = models.CharField(max_length=40)
    venta_o_alquiler = models.BooleanField()
    otros_atributos = models.CharField(max_length=40)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    preferencias = models.CharField(max_length=40)

class Agentes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    especialidad = models.CharField(max_length=40)

class Testimonios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    testimonios = models.CharField(max_length=40)

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    agendar_visita = models.BooleanField()

class Servicios(models.Model):
    nombre = models.CharField(max_length=40)
    servicio = models.CharField(max_length=40)

class Noticias(models.Model):
    fecha = models.DateField()
    noticia = models.CharField(max_length=40)