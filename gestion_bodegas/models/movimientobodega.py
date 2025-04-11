from django.db import models  # Importamos el módulo `models` de Django para definir modelos.
from .material import Material
from .bodega.bodega import Bodega

# ------------------- MODELO MOVIMIENTO DE BODEGA -------------------
class MovimientoBodega(models.Model):
    # Representa un movimiento de entrada o salida de materiales en una bodega.
    TIPOS_MOVIMIENTO = [  # Opciones para el tipo de movimiento.
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPOS_MOVIMIENTO)  # Tipo de movimiento (entrada o salida).
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  # Material involucrado en el movimiento.
    cantidad = models.PositiveIntegerField()  # Cantidad de material movido (valor positivo).
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora del movimiento (se asigna automáticamente).
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)  # Bodega donde ocurre el movimiento.