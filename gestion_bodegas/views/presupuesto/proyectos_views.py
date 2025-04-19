from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.forms import ModelForm
from django import forms
from ...models.presupuesto import Proyecto

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto_total']

class ListarProyectos(ListView):
    model = Proyecto
    print(Proyecto.objects.all())
    template_name = 'gestion_bodegas/presupuesto/listar_proyecto.html'
    context_object_name = 'proyectos'

class DetalleProyecto(DetailView):
    model = Proyecto
    template_name = 'gestion_bodegas/presupuesto/detalle_proyecto.html'
    context_object_name = 'proyecto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partidas'] = self.object.partidas.all()
        return context
    
class CrearProyecto(CreateView):
    model = Proyecto
    template_name = 'gestion_bodegas/presupuesto/crear_proyecto.html'
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto_total']
    success_url = reverse_lazy('listar_proyectos')

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto_total']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),  
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),   
        }
        

class EditarProyecto(UpdateView):
    model = Proyecto
    template_name = 'gestion_bodegas/presupuesto/editar_proyecto.html'
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto_total']
    success_url = reverse_lazy('listar_proyectos')
