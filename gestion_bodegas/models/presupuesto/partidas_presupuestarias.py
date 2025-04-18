from django.db import models
from .proyectos import Proyecto

class PartidasPresupuestarias(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='partidas')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    costo_estimado = models.DecimalField(max_digits=15, decimal_places=2)
    costo_real = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre