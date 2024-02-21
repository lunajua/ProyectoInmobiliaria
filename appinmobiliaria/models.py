from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


opciones_propiedad = [
    [1, "Departamento"],
    [2, "Casa Country"],
    [3, "Casa Residencial"],
    [4, "Oficina"],
    [5, "Proyecto de Construcción"],
    [6, "Condominio"],
    [7, "Comercio"],
    [8, "Garage"]
]

ven_alq = [
    [1, "Venta"],
    [2, "Alquiler"],
]
class Propiedad(models.Model):
    direccion = models.CharField(max_length=40)
    tipo_de_propiedad = models.CharField(max_length=40, choices=opciones_propiedad)
    localizacion = models.CharField(max_length=40)
    palabra_clave = models.CharField(max_length=40)
    metros = models.IntegerField(validators=[MinValueValidator(0)])
    ambientes = models.IntegerField(validators=[MinValueValidator(0)])
    banos = models.IntegerField(validators=[MinValueValidator(0)])
    descripcion = models.CharField(max_length=40)
    venta_o_alquiler =models.CharField(max_length=40, choices=ven_alq)
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