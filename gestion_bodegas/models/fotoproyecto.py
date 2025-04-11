from django.db import models  # Importamos el módulo `models` de Django para definir modelos.
from .proyecto import Proyecto

# ------------------- MODELO FOTO DE PROYECTO -------------------
class FotoProyecto(models.Model):
    # Representa una foto asociada a un proyecto.
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="fotos")
    # Proyecto al que pertenece la foto.
    imagen = models.ImageField(upload_to="proyectos/")  # Imagen de la foto (se guarda en la carpeta "proyectos/").
    descripcion = models.TextField(blank=True, null=True)  # Descripción de la foto (opcional).
    fecha_subida = models.DateTimeField(auto_now_add=True)  # Fecha y hora de subida de la foto (automática).