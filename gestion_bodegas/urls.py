from django.urls import path
from .views import (
    login_view, logout_view, index,
    clientes, register_cliente,
    proyectos, register_project,
    materiales, register_material, edit_material, delete_material,
    movimientos, register_movimiento,
    evidencias, upload_foto,
    register_user,
)

urlpatterns = [
    # Autenticación
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Página principal
    path('index/', index, name='index'),

    # Cliente
    path('clientes/', clientes, name='clientes'),
    path('clientes/registrar/', register_cliente, name='register_cliente'),

    # Proyecto
    path('proyectos/', proyectos, name='proyectos'),
    path('proyectos/registrar/', register_project, name='register_project'),

    # Material
    path('materiales/', materiales, name='materiales'),
    path('materiales/registrar/', register_material, name='register_material'),
    path('materiales/editar/<int:pk>/', edit_material, name='edit_material'),
    path('materiales/eliminar/<int:pk>/', delete_material, name='delete_material'),

    # Movimiento
    path('movimientos/', movimientos, name='movimientos'),
    path('movimientos/registrar/', register_movimiento, name='register_movimiento'),

    # Evidencias
    path('evidencias/', evidencias, name='evidencias'),
    path('fotos/subir/', upload_foto, name='upload_foto'),

    # Usuario
    path('usuarios/registrar/', register_user, name='register_user'),
]
