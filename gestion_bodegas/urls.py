# Importamos la función `path` de Django para definir las rutas de la aplicación.
# También importamos el módulo `views` que contiene las funciones que manejarán las solicitudes para cada ruta.
from django.urls import path
from . import views

# Definimos una lista llamada `urlpatterns` que contiene todas las rutas (URLs) de la aplicación.
# Cada ruta está asociada a una vista específica en el archivo `views.py`.

urlpatterns = [
    # Ruta para la página de inicio de sesión.
    # Cuando el usuario accede a la raíz del sitio ('/'), se ejecuta la vista `login_view`.
    path('', views.login_view, name='login'),

    # Ruta para la página principal (dashboard) de la aplicación.
    # Requiere que el usuario esté autenticado. La vista `index` se encarga de renderizar esta página.
    path('index/', views.index, name='index'),

    # Ruta para listar los clientes registrados en el sistema.
    # La vista `clientes` obtiene los datos de los clientes y los muestra en una plantilla.
    path('clientes/', views.clientes, name='clientes'),

    # Ruta para listar los proyectos registrados en el sistema.
    # La vista `proyectos` se encarga de mostrar esta información.
    path('proyectos/', views.proyectos, name='proyectos'),

    # Ruta para registrar un nuevo usuario.
    # Solo los administradores pueden acceder a esta vista (`register_user`).
    path('register_user/', views.register_user, name='register_user'),

    # Ruta para registrar un nuevo proyecto.
    # La vista `register_project` permite a los administradores agregar proyectos al sistema.
    path('register_project/', views.register_project, name='register_project'),

    # Ruta para registrar un nuevo material.
    # La vista `register_material` permite a los administradores agregar materiales al sistema.
    path('register_material/', views.register_material, name='register_material'),

    # Ruta para registrar un nuevo movimiento de bodega.
    # La vista `register_movimiento` permite registrar entradas o salidas de materiales en la bodega.
    path('register_movimiento/', views.register_movimiento, name='register_movimiento'),

    # Ruta para registrar un nuevo cliente.
    # La vista `register_cliente` permite a los administradores agregar clientes al sistema.
    path('register_cliente/', views.register_cliente, name='register_cliente'),

    # Ruta para subir una foto asociada a un proyecto.
    # La vista `upload_foto` permite a los usuarios autenticados cargar imágenes.
    path('upload_foto/', views.upload_foto, name='upload_foto'),

    # Ruta para listar todos los materiales registrados en el sistema.
    # La vista `materiales` muestra esta información.
    path('materiales/', views.materiales, name='materiales'),

    # Ruta para editar un material existente.
    # La vista `edit_material` permite modificar los datos de un material específico identificado por su `pk` (clave primaria).
    path('edit_material/<int:pk>/', views.edit_material, name='edit_material'),

    # Ruta para eliminar un material existente.
    # La vista `delete_material` permite eliminar un material específico identificado por su `pk`.
    path('delete_material/<int:pk>/', views.delete_material, name='delete_material'),

    # Ruta para listar los movimientos de bodega.
    # La vista `movimientos` muestra las entradas y salidas de materiales en la bodega.
    path('movimientos/', views.movimientos, name='movimientos'),

    # Ruta para listar las evidencias (fotos) asociadas a proyectos.
    # La vista `evidencias` muestra las imágenes cargadas en el sistema.
    path('evidencias/', views.evidencias, name='evidencias'),

    # Ruta para cerrar sesión.
    # La vista `logout_view` cierra la sesión del usuario y lo redirige a la página de inicio de sesión.
    path('logout/', views.logout_view, name='logout'),
]