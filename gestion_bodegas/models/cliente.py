from django.db import models  # Importamos el módulo `models` de Django para definir modelos.

# ------------------- MODELO CLIENTE -------------------
class Cliente(models.Model):
    # Representa a un cliente en el sistema.
    nombre = models.CharField(max_length=255)  # Nombre del cliente (máximo 255 caracteres).
    contacto = models.CharField(max_length=100, blank=True, null=True)  # Persona de contacto (opcional).
    telefono = models.CharField(max_length=20, blank=True, null=True)  # Teléfono del cliente (opcional).
    email = models.EmailField(unique=True)  # Correo electrónico único para cada cliente.
    direccion = models.TextField(blank=True, null=True)  # Dirección del cliente (opcional).

