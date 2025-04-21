from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from gestion_bodegas.models.articulos.articulos import Articulo

# Vista para listar artículos
def listar_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulos/listar.html', {'articulos': articulos})

# Vista para crear un nuevo artículo
def crear_articulo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo_rfid = request.POST.get('codigo_rfid')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        ubicacion_actual = request.POST.get('ubicacion_actual')
        responsable = request.POST.get('responsable')
        estado = request.POST.get('estado')

        Articulo.objects.create(
            nombre=nombre,
            codigo_rfid=codigo_rfid,
            descripcion=descripcion,
            categoria=categoria,
            ubicacion_actual=ubicacion_actual,
            responsable=responsable,
            estado=estado
        )
        return redirect(reverse('listar_articulos'))
    return render(request, 'articulos/crear.html')

# Vista para editar un artículo existente
def editar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        articulo.nombre = request.POST.get('nombre')
        articulo.codigo_rfid = request.POST.get('codigo_rfid')
        articulo.descripcion = request.POST.get('descripcion')
        articulo.categoria = request.POST.get('categoria')
        articulo.ubicacion_actual = request.POST.get('ubicacion_actual')
        articulo.responsable = request.POST.get('responsable')
        articulo.estado = request.POST.get('estado')
        articulo.save()
        return redirect(reverse('listar_articulos'))
    return render(request, 'articulos/editar.html', {'articulo': articulo})

# Vista para eliminar un artículo
def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        articulo.delete()
        return redirect(reverse('listar_articulos'))
    return render(request, 'articulos/eliminar.html', {'articulo': articulo})