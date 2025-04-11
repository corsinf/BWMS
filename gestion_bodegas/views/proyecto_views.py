from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Proyecto
from ..forms import ProyectoForm

def is_admin(user):
    return user.is_superuser

@login_required
def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'gestion_bodegas/proyectos.html', {'proyectos': proyectos})

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
