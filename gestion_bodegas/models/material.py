from django.db import models  # Importamos el módulo `models` de Django para definir modelos.

# ------------------- MODELO MATERIAL -------------------
class Material(models.Model):
    # Representa un material que puede ser utilizado en proyectos.
    nombre = models.CharField(max_length=255)  # Nombre del material.
    descripcion = models.TextField(blank=True, null=True)  # Descripción del material (opcional).
    stock = models.PositiveIntegerField(default=0)  # Cantidad disponible en stock (valor positivo).
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por unidad del material.