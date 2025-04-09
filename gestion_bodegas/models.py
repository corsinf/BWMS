from django.db import models  # Importamos el módulo `models` de Django para definir modelos.

# ------------------- MODELO CLIENTE -------------------
class Cliente(models.Model):
    # Representa a un cliente en el sistema.
    nombre = models.CharField(max_length=255)  # Nombre del cliente (máximo 255 caracteres).
    contacto = models.CharField(max_length=100, blank=True, null=True)  # Persona de contacto (opcional).
    telefono = models.CharField(max_length=20, blank=True, null=True)  # Teléfono del cliente (opcional).
    email = models.EmailField(unique=True)  # Correo electrónico único para cada cliente.
    direccion = models.TextField(blank=True, null=True)  # Dirección del cliente (opcional).

# ------------------- MODELO PROYECTO -------------------
class Proyecto(models.Model):
    # Representa un proyecto asociado a un cliente.
    ESTADOS = [  # Opciones para el estado del proyecto.
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    nombre = models.CharField(max_length=255)  # Nombre del proyecto.
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')  # Estado actual del proyecto.
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="proyectos")
    # Relación con el cliente. Si el cliente se elimina, también se eliminan sus proyectos.

# ------------------- MODELO MATERIAL -------------------
class Material(models.Model):
    # Representa un material que puede ser utilizado en proyectos.
    nombre = models.CharField(max_length=255)  # Nombre del material.
    descripcion = models.TextField(blank=True, null=True)  # Descripción del material (opcional).
    stock = models.PositiveIntegerField(default=0)  # Cantidad disponible en stock (valor positivo).
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por unidad del material.

# ------------------- MODELO BODEGA -------------------
class Bodega(models.Model):
    # Representa una bodega donde se almacenan materiales.
    nombre = models.CharField(max_length=255)  # Nombre de la bodega.
    ubicacion = models.TextField(blank=True, null=True)  # Ubicación de la bodega (opcional).

# ------------------- MODELO MOVIMIENTO DE BODEGA -------------------
class MovimientoBodega(models.Model):
    # Representa un movimiento de entrada o salida de materiales en una bodega.
    TIPOS_MOVIMIENTO = [  # Opciones para el tipo de movimiento.
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPOS_MOVIMIENTO)  # Tipo de movimiento (entrada o salida).
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  # Material involucrado en el movimiento.
    cantidad = models.PositiveIntegerField()  # Cantidad de material movido (valor positivo).
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora del movimiento (se asigna automáticamente).
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)  # Bodega donde ocurre el movimiento.

# ------------------- MODELO ENTREGA DE MATERIAL -------------------
class EntregaMaterial(models.Model):
    # Representa la entrega de un material a un proyecto.
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="entregas")
    # Proyecto al que se entrega el material.
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  # Material entregado.
    cantidad = models.PositiveIntegerField()  # Cantidad de material entregado.
    fecha_entrega = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la entrega (automática).

# ------------------- MODELO ACTA DE ENTREGA -------------------
class ActaEntrega(models.Model):
    # Representa un acta de entrega asociada a un proyecto.
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="actas")
    # Proyecto al que pertenece el acta.
    descripcion = models.TextField()  # Descripción del acta.
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación del acta (automática).
    archivo = models.FileField(upload_to="actas/")  # Archivo del acta (se guarda en la carpeta "actas/").

# ------------------- MODELO FOTO DE PROYECTO -------------------
class FotoProyecto(models.Model):
    # Representa una foto asociada a un proyecto.
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="fotos")
    # Proyecto al que pertenece la foto.
    imagen = models.ImageField(upload_to="proyectos/")  # Imagen de la foto (se guarda en la carpeta "proyectos/").
    descripcion = models.TextField(blank=True, null=True)  # Descripción de la foto (opcional).
    fecha_subida = models.DateTimeField(auto_now_add=True)  # Fecha y hora de subida de la foto (automática).