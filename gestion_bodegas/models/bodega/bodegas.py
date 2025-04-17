from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre