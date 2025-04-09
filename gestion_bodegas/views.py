# Importaciones necesarias para las vistas
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Importación de modelos
from .models import Cliente, Proyecto, Material, Bodega, MovimientoBodega, FotoProyecto

# Importación de formularios
from .forms import UserForm, ProyectoForm, MaterialForm, MovimientoBodegaForm, FotoProyectoForm, ClienteForm

# Función para verificar si un usuario es administrador
def is_admin(user):
    return user.is_superuser

# ------------------- AUTENTICACIÓN -------------------

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'gestion_bodegas/login.html', {'form': form})

# Vista de cierre de sesión
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# ------------------- VISTAS GENERALES -------------------

# Vista principal protegida por login
@login_required
def index(request):
    return render(request, 'gestion_bodegas/index.html')

# Vista para listar clientes (requiere autenticación)
@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion_bodegas/clientes.html', {'clientes': clientes})

# Vista para listar proyectos (requiere autenticación)
@login_required
def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestion_bodegas/proyectos.html', {'proyectos': proyectos})

# Vista para listar materiales (requiere autenticación)
@login_required
def materiales(request):
    materiales = Material.objects.all()
    return render(request, 'gestion_bodegas/materiales.html', {'materiales': materiales})

# Vista para listar movimientos de bodega (requiere autenticación)
@login_required
def movimientos(request):
    movimientos = MovimientoBodega.objects.all()
    return render(request, 'gestion_bodegas/movimientos.html', {'movimientos': movimientos})

# Vista para listar evidencias (fotos) (requiere autenticación)
@login_required
def evidencias(request):
    fotos = FotoProyecto.objects.all()
    return render(request, 'gestion_bodegas/evidencias.html', {'fotos': fotos})

# ------------------- REGISTRO DE ENTIDADES -------------------

# Vista para registrar un usuario (solo administradores)
@login_required
@user_passes_test(is_admin)
def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'gestion_bodegas/register_user.html', {'form': form})

# Vista para registrar un proyecto (solo administradores)
@login_required
@user_passes_test(is_admin)
def register_project(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProyectoForm()
    return render(request, 'gestion_bodegas/register_project.html', {'form': form})

# Vista para registrar material (solo administradores)
@login_required
@user_passes_test(is_admin)
def register_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MaterialForm()
    return render(request, 'gestion_bodegas/register_material.html', {'form': form})

# Vista para registrar movimientos de bodega (solo administradores)
@login_required
@user_passes_test(is_admin)
def register_movimiento(request):
    if request.method == 'POST':
        form = MovimientoBodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovimientoBodegaForm()
    return render(request, 'gestion_bodegas/register_movimiento.html', {'form': form})

# Vista para registrar un cliente (solo administradores)
@login_required
@user_passes_test(is_admin)
def register_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'gestion_bodegas/register_cliente.html', {'form': form})

# ------------------- SUBIDA DE FOTOS -------------------

# Vista para subir fotos asociadas a proyectos (requiere autenticación)
@login_required
def upload_foto(request):
    if request.method == 'POST':
        form = FotoProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FotoProyectoForm()
    return render(request, 'gestion_bodegas/upload_foto.html', {'form': form})

# ------------------- EDICIÓN Y ELIMINACIÓN DE MATERIALES -------------------

# Vista para editar un material (solo administradores)
@login_required
@user_passes_test(is_admin)
def edit_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('materiales')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'gestion_bodegas/edit_material.html', {'form': form})

# Vista para eliminar un material (solo administradores)
@login_required
@user_passes_test(is_admin)
def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('materiales')
    return render(request, 'gestion_bodegas/delete_material.html', {'material': material})