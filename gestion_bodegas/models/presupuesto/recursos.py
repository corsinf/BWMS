from django.db import models

class Recursos(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField(blank=True, null=True)  
    tipo = models.CharField(max_length=50)  
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  
    costo_unitario = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)  

    def __str__(self):
        return self.nombre
