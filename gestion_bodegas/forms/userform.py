from django import forms  # Importamos el módulo `forms` de Django para crear formularios.
from django.contrib.auth.models import User  # Importamos el modelo `User` para gestionar usuarios.
from ..models import Proyecto, Cliente, Material, FotoProyecto  # Importamos los modelos necesarios.

# ------------------- FORMULARIO DE USUARIO -------------------
class UserForm(forms.ModelForm):
    # Formulario para registrar o editar usuarios.
    password = forms.CharField(widget=forms.PasswordInput)  # Campo de contraseña con un widget para ocultar el texto.
    
    class Meta:
        model = User  # Basado en el modelo `User` de Django.
        fields = ['username', 'email', 'password', 'is_superuser']  # Campos que se incluirán en el formulario.
