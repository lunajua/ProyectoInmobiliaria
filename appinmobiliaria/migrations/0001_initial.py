# Generated by Django 4.2 on 2024-02-27 00:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('agendar_visita', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=40)),
                ('tipo_de_propiedad', models.IntegerField(choices=[[1, 'Departamento'], [2, 'Casa Country'], [3, 'Casa Residencial'], [4, 'Oficina'], [5, 'Proyecto de Construcción'], [6, 'Condominio'], [7, 'Comercio'], [8, 'Garage']])),
                ('localidad', models.CharField(max_length=40)),
                ('palabra_clave', models.CharField(max_length=40)),
                ('metros', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('ambientes', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('baños', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('descripcion', models.TextField()),
                ('venta_o_alquiler', models.IntegerField(choices=[[1, 'Venta'], [2, 'Alquiler']])),
                ('otros_atributos', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='appinmobiliaria.propiedad')),
            ],
        ),
    ]
