from django.urls import path
from .views import (
    login_view, logout_view, index,
    clientes, register_cliente,
    proyectos, register_project,
    materiales, register_material, edit_material, delete_material,
    evidencias, upload_foto,
    register_user,
)

from .views.bodega import (
    bodegas_views,
    articulos_views,
    inventario_views,
    ubicaciones_views,
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

    # Evidencias
    path('evidencias/', evidencias, name='evidencias'),
    path('fotos/subir/', upload_foto, name='upload_foto'),

    # Usuario
    path('usuarios/registrar/', register_user, name='register_user'),
    
    # URLs para Bodegas
    path('bodegas/', bodegas_views.ListaBodegas.as_view(), name='lista_bodegas'),
    path('bodegas/crear/', bodegas_views.CrearBodega.as_view(), name='crear_bodega'),
    path('bodegas/editar/<int:pk>/', bodegas_views.EditarBodega.as_view(), name='editar_bodega'),
    path('bodegas/eliminar/<int:pk>/', bodegas_views.EliminarBodega.as_view(), name='eliminar_bodega'),
    path('bodegas/<int:bodega_id>/articulos/', bodegas_views.ListaArticulosPorBodega.as_view(), name='articulos_por_bodega'),

    # URLs para Artículos
    path('articulos/', articulos_views.ListaArticulos.as_view(), name='lista_articulos'),
    path('articulos/crear/', articulos_views.CrearArticulo.as_view(), name='crear_articulo'),
    path('articulos/editar/<int:pk>/', articulos_views.EditarArticulo.as_view(), name='editar_articulo'),
    path('articulos/eliminar/<int:pk>/', articulos_views.EliminarArticulo.as_view(), name='eliminar_articulo'),

    # URLs para Inventario
    path('inventario/', inventario_views.ListaInventario.as_view(), name='lista_inventario'),
    path('inventario/crear/', inventario_views.CrearInventario.as_view(), name='crear_inventario'),
    path('inventario/editar/<int:pk>/', inventario_views.EditarInventario.as_view(), name='editar_inventario'),
    path('inventario/eliminar/<int:pk>/', inventario_views.EliminarInventario.as_view(), name='eliminar_inventario'),

    # URLs para Zonas
    path('ubicaciones/zonas/', ubicaciones_views.ListaZonas.as_view(), name='lista_zonas'),
    path('ubicaciones/zonas/crear/', ubicaciones_views.CrearZona.as_view(), name='crear_zona'),
    path('ubicaciones/zonas/editar/<int:pk>/', ubicaciones_views.EditarZona.as_view(), name='editar_zona'),
    path('ubicaciones/zonas/eliminar/<int:pk>/', ubicaciones_views.EliminarZona.as_view(), name='eliminar_zona'),

    # URLs para Estanterías
    path('ubicaciones/estanterias/', ubicaciones_views.ListaEstanterias.as_view(), name='lista_estanterias'),
    path('ubicaciones/estanterias/crear/', ubicaciones_views.CrearEstanteria.as_view(), name='crear_estanteria'),
    path('ubicaciones/estanterias/editar/<int:pk>/', ubicaciones_views.EditarEstanteria.as_view(), name='editar_estanteria'),
    path('ubicaciones/estanterias/eliminar/<int:pk>/', ubicaciones_views.EliminarEstanteria.as_view(), name='eliminar_estanteria'),

    # URLs para Niveles
    path('ubicaciones/niveles/', ubicaciones_views.ListaNiveles.as_view(), name='lista_niveles'),
    path('ubicaciones/niveles/crear/', ubicaciones_views.CrearNivel.as_view(), name='crear_nivel'),
    path('ubicaciones/niveles/editar/<int:pk>/', ubicaciones_views.EditarNivel.as_view(), name='editar_nivel'),
    path('ubicaciones/niveles/eliminar/<int:pk>/', ubicaciones_views.EliminarNivel.as_view(), name='eliminar_nivel'),
]
