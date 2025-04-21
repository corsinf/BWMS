from django.db import models
from django.utils.timezone import now

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_rfid = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, default='General')  # Valor predeterminado
    ubicacion_actual = models.CharField(max_length=200, default='Almacén Principal')  # Valor predeterminado
    responsable = models.CharField(max_length=100, default='No asignado')  # Valor predeterminado
    estado = models.CharField(
        max_length=50,
        choices=[
            ('activo', 'Activo'),
            ('inactivo', 'Inactivo'),
            ('mantenimiento', 'Mantenimiento'),
        ],
        default='activo'  # Valor predeterminado
    )
    fecha_ingreso = models.DateTimeField(default=now)  # Valor predeterminado
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo_rfid})"