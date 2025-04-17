from django import forms  # Importamos el módulo `forms` de Django para crear formularios.
from django.contrib.auth.models import User  # Importamos el modelo `User` para gestionar usuarios.
from ..models import Proyecto, Cliente, Material, FotoProyecto  # Importamos los modelos necesarios.

# ------------------- FORMULARIO DE CLIENTE -------------------
class ClienteForm(forms.ModelForm):
    # Formulario para registrar o editar clientes.
    class Meta:
        model = Cliente  # Basado en el modelo `Cliente`.
        fields = ['nombre', 'contacto', 'telefono', 'email', 'direccion']  # Campos que se incluirán en el formulario.