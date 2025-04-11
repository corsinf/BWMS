from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Material
from ..forms import MaterialForm

def is_admin(user):
    return user.is_superuser

@login_required
def materiales(request):
    materiales = Material.objects.all()
    return render(request, 'gestion_bodegas/materiales.html', {'materiales': materiales})

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

@login_required
@user_passes_test(is_admin)
def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('materiales')
    return render(request, 'gestion_bodegas/delete_material.html', {'material': material})
