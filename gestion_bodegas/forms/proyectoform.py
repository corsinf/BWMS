from django import forms  # Importamos el módulo `forms` de Django para crear formularios.
from django.contrib.auth.models import User  # Importamos el modelo `User` para gestionar usuarios.
from ..models import Proyecto, Cliente, Material, FotoProyecto  # Importamos los modelos necesarios.

# ------------------- FORMULARIO DE PROYECTO -------------------
class ProyectoForm(forms.ModelForm):
    # Formulario para registrar o editar proyectos.
    class Meta:
        model = Proyecto  # Basado en el modelo `Proyecto`.
        fields = ['nombre', 'estado', 'cliente']  # Campos que se incluirán en el formulario.
