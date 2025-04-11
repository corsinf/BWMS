from django.db import models  # Importamos el módulo `models` de Django para definir modelos.

# ------------------- MODELO BODEGA -------------------
class Bodega(models.Model):
    # Representa una bodega donde se almacenan materiales.
    nombre = models.CharField(max_length=255)  # Nombre de la bodega.
    ubicacion = models.TextField(blank=True, null=True)  # Ubicación de la bodega (opcional).