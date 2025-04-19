from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto_total = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'gestion_bodegas_proyecto'

