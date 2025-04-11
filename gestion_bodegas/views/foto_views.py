from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import FotoProyecto
from ..forms import FotoProyectoForm

@login_required
def evidencias(request):
    fotos = FotoProyecto.objects.all()
    return render(request, 'gestion_bodegas/evidencias.html', {'fotos': fotos})

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
