from django.db import models  # Importamos el módulo `models` de Django para definir modelos.
from .presupuesto import Proyecto

# ------------------- MODELO ACTA DE ENTREGA -------------------
class ActaEntrega(models.Model):
    # Representa un acta de entrega asociada a un proyecto.
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="actas")
    # Proyecto al que pertenece el acta.
    descripcion = models.TextField()  # Descripción del acta.
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación del acta (automática).
    archivo = models.FileField(upload_to="actas/")  # Archivo del acta (se guarda en la carpeta "actas/").