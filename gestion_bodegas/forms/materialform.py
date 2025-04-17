from django import forms  # Importamos el módulo `forms` de Django para crear formularios.
from django.contrib.auth.models import User  # Importamos el modelo `User` para gestionar usuarios.
from ..models import Proyecto, Cliente, Material, FotoProyecto  # Importamos los modelos necesarios.

# ------------------- FORMULARIO DE MATERIAL -------------------
class MaterialForm(forms.ModelForm):
    # Formulario para registrar o editar materiales.
    class Meta:
        model = Material  # Basado en el modelo `Material`.
        fields = ['nombre', 'descripcion', 'stock', 'precio_unitario']  # Campos que se incluirán en el formulario.
