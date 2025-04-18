from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from ...models.presupuesto.recursos import Recursos
from ...models.presupuesto import PartidasPresupuestarias

class ListarRecursos(ListView):
    model = Recursos
    template_name = 'presupuesto/listar_recursos.html'
    context_object_name = 'recursos'

    def get_queryset(self):
        return Recursos.objects.filter(partida_id=self.kwargs['partida_id'])

class DetalleRecurso(DetailView):
    model = Recursos
    template_name = 'presupuesto/detalle_recurso.html'
    context_object_name = 'recurso'

class CrearRecurso(CreateView):
    model = Recursos
    template_name = 'gestion_bodegas/presupuesto/crear_recurso.html'
    fields = ['tipo', 'descripcion', 'cantidad', 'costo_unitario']

    def form_valid(self, form):
        form.instance.partida = PartidasPresupuestarias.objects.get(id=self.kwargs['partida_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listar_recursos', kwargs={'partida_id': self.kwargs['partida_id']})

class EditarRecurso(UpdateView):
    model = Recursos
    template_name = 'gestion_bodegas/presupuesto/editar_recurso.html'
    fields = ['tipo', 'descripcion', 'cantidad', 'costo_unitario']

    def get_success_url(self):
        return reverse_lazy('listar_recursos', kwargs={'partida_id': self.object.partida.id})
