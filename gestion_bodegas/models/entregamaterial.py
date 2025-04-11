from django.db import models  # Importamos el módulo `models` de Django para definir modelos.
from .proyecto import Proyecto
from .material import Material

# ------------------- MODELO ENTREGA DE MATERIAL -------------------
class EntregaMaterial(models.Model):
    # Representa la entrega de un material a un proyecto.
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="entregas")
    # Proyecto al que se entrega el material.
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  # Material entregado.
    cantidad = models.PositiveIntegerField()  # Cantidad de material entregado.
    fecha_entrega = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la entrega (automática).