from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from ...models.presupuesto import Proyecto

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
        # Asegúrate de que las partidas están disponibles
        context['partidas'] = self.object.partidas.all()
        return context
    
class CrearProyecto(CreateView):
    model = Proyecto
    template_name = 'gestion_bodegas/presupuesto/crear_proyecto.html'
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto_total']
    success_url = reverse_lazy('listar_proyectos')

class EditarProyecto(UpdateView):
    model = Proyecto
    template_name = 'gestion_bodegas/presupuesto/editar_proyecto.html'
    fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'presupuesto_total']
    success_url = reverse_lazy('listar_proyectos')
