from django.db import models

# Create your models here.


class Parqueadero(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
