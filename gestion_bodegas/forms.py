from django import forms  # Importamos el módulo `forms` de Django para crear formularios.
from django.contrib.auth.models import User  # Importamos el modelo `User` para gestionar usuarios.
from .models import Proyecto, Cliente, Material, MovimientoBodega, FotoProyecto  # Importamos los modelos necesarios.

# ------------------- FORMULARIO DE USUARIO -------------------
class UserForm(forms.ModelForm):
    # Formulario para registrar o editar usuarios.
    password = forms.CharField(widget=forms.PasswordInput)  # Campo de contraseña con un widget para ocultar el texto.
    
    class Meta:
        model = User  # Basado en el modelo `User` de Django.
        fields = ['username', 'email', 'password', 'is_superuser']  # Campos que se incluirán en el formulario.

# ------------------- FORMULARIO DE PROYECTO -------------------
class ProyectoForm(forms.ModelForm):
    # Formulario para registrar o editar proyectos.
    class Meta:
        model = Proyecto  # Basado en el modelo `Proyecto`.
        fields = ['nombre', 'estado', 'cliente']  # Campos que se incluirán en el formulario.

# ------------------- FORMULARIO DE MATERIAL -------------------
class MaterialForm(forms.ModelForm):
    # Formulario para registrar o editar materiales.
    class Meta:
        model = Material  # Basado en el modelo `Material`.
        fields = ['nombre', 'descripcion', 'stock', 'precio_unitario']  # Campos que se incluirán en el formulario.

# ------------------- FORMULARIO DE MOVIMIENTO DE BODEGA -------------------
class MovimientoBodegaForm(forms.ModelForm):
    # Formulario para registrar movimientos de entrada o salida en una bodega.
    class Meta:
        model = MovimientoBodega  # Basado en el modelo `MovimientoBodega`.
        fields = ['tipo', 'material', 'cantidad', 'bodega']  # Campos que se incluirán en el formulario.

# ------------------- FORMULARIO DE FOTO DE PROYECTO -------------------
class FotoProyectoForm(forms.ModelForm):
    # Formulario para subir fotos asociadas a proyectos.
    class Meta:
        model = FotoProyecto  # Basado en el modelo `FotoProyecto`.
        fields = ['proyecto', 'imagen', 'descripcion']  # Campos que se incluirán en el formulario.

# ------------------- FORMULARIO DE CLIENTE -------------------
class ClienteForm(forms.ModelForm):
    # Formulario para registrar o editar clientes.
    class Meta:
        model = Cliente  # Basado en el modelo `Cliente`.
        fields = ['nombre', 'contacto', 'telefono', 'email', 'direccion']  # Campos que se incluirán en el formulario.