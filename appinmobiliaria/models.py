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
    tipo_de_propiedad = models.IntegerField(choices=opciones_propiedad)
    localidad = models.CharField(max_length=40)
    palabra_clave = models.CharField(max_length=40)
    metros = models.IntegerField(validators=[MinValueValidator(0)])
    ambientes = models.IntegerField(validators=[MinValueValidator(0)])
    baños = models.IntegerField(validators=[MinValueValidator(0)])
    descripcion = models.TextField()
    venta_o_alquiler =models.IntegerField(choices=ven_alq)
    otros_atributos = models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"dirección {self.direccion} | precio: {self.otros_atributos} | cantidad de ambientes: {self.ambientes}"


class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    agendar_visita = models.BooleanField()
    
    def __str__(self):
        return self.nombre + " " + self.apellido


class Image(models.Model):
    propiedad = models.ForeignKey(Propiedad, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
