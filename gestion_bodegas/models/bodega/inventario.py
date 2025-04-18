from django.db import models
from .bodegas import Bodega
from .articulos import Articulo
from .ubicaciones import Zona, Estanteria, Nivel

class InventarioBodega(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='inventario')
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='inventario')
    cantidad = models.PositiveIntegerField(default=0)
    zona = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True, blank=True)
    estanteria = models.ForeignKey(Estanteria, on_delete=models.SET_NULL, null=True, blank=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('bodega', 'articulo', 'zona', 'estanteria', 'nivel') # La ubicación ahora también forma parte de la unicidad

    def __str__(self):
        ubicacion_str = ""
        if self.zona:
            ubicacion_str += f"Zona: {self.zona.nombre}"
        if self.estanteria:
            if ubicacion_str:
                ubicacion_str += ", "
            ubicacion_str += f"Estantería: {self.estanteria.nombre}"
        if self.nivel:
            if ubicacion_str:
                ubicacion_str += ", "
            ubicacion_str += f"Nivel: {self.nivel.nombre}"
        return f"{self.articulo.nombre} en {self.bodega.nombre} ({self.cantidad}) - Ubicación: {ubicacion_str if ubicacion_str else 'Sin ubicación'}"

# Modelos Adicionales (Opcionales)

class TransaccionInventario(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='transacciones')
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='transacciones')
    # Puedes añadir campos para el usuario que realizó la transacción, etc.

    def __str__(self):
        return f"{self.tipo} de {self.articulo.nombre} en {self.bodega.nombre} ({self.cantidad} el {self.fecha})"

class HistorialMovimiento(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='movimientos')
    bodega_origen = models.ForeignKey(Bodega, on_delete=models.SET_NULL, null=True, related_name='salidas')
    bodega_destino = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='entradas')
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()
    # Puedes añadir información sobre el usuario que realizó la transferencia

    def __str__(self):
        return f"Transferencia de {self.articulo.nombre} de {self.bodega_origen} a {self.bodega_destino} ({self.cantidad} el {self.fecha})"

# Si necesitas gestión de usuarios y roles, podrías definir modelos aquí o usar los modelos de Django Auth.