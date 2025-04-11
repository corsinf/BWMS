from django.db import models  # Importamos el módulo `models` de Django para definir modelos.
from .cliente import Cliente

# ------------------- MODELO PROYECTO -------------------
class Proyecto(models.Model):
    # Representa un proyecto asociado a un cliente.
    ESTADOS = [  # Opciones para el estado del proyecto.
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    nombre = models.CharField(max_length=255)  # Nombre del proyecto.
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')  # Estado actual del proyecto.
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="proyectos")
    # Relación con el cliente. Si el cliente se elimina, también se eliminan sus proyectos.