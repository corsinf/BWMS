from django import forms  # Importamos el módulo `forms` de Django para crear formularios.
from django.contrib.auth.models import User  # Importamos el modelo `User` para gestionar usuarios.
from ..models import Proyecto, Cliente, Material, FotoProyecto  # Importamos los modelos necesarios.

# ------------------- FORMULARIO DE FOTO DE PROYECTO -------------------
class FotoProyectoForm(forms.ModelForm):
    # Formulario para subir fotos asociadas a proyectos.
    class Meta:
        model = FotoProyecto  # Basado en el modelo `FotoProyecto`.
        fields = ['proyecto', 'imagen', 'descripcion']  # Campos que se incluirán en el formulario.