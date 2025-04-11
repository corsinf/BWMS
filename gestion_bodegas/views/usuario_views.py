from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from ..forms import UserForm

def is_admin(user):
    return user.is_superuser

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
