from django.db import models
from .bodegas import Bodega

class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='zonas')

    class Meta:
        unique_together = ('nombre', 'bodega')

    def __str__(self):
        return f"{self.nombre} (Bodega: {self.bodega.nombre})"

class Estanteria(models.Model):
    nombre = models.CharField(max_length=100)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='estanterias')

    class Meta:
        unique_together = ('nombre', 'zona')

    def __str__(self):
        return f"{self.nombre} (Zona: {self.zona.nombre}, Bodega: {self.zona.bodega.nombre})"

class Nivel(models.Model):
    nombre = models.CharField(max_length=100)
    estanteria = models.ForeignKey(Estanteria, on_delete=models.CASCADE, related_name='niveles')

    class Meta:
        unique_together = ('nombre', 'estanteria')

    def __str__(self):
        return f"{self.nombre} (Estantería: {self.estanteria.nombre}, Zona: {self.estanteria.zona.nombre}, Bodega: {self.estanteria.zona.bodega.nombre})"