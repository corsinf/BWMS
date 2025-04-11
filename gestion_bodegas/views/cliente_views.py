from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Cliente
from ..forms import ClienteForm

def is_admin(user):
    return user.is_superuser

@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion_bodegas/clientes.html', {'clientes': clientes})

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
