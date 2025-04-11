from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import MovimientoBodega
from ..forms import MovimientoBodegaForm

def is_admin(user):
    return user.is_superuser

@login_required
def movimientos(request):
    movimientos = MovimientoBodega.objects.all()
    return render(request, 'gestion_bodegas/movimientos.html', {'movimientos': movimientos})

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
