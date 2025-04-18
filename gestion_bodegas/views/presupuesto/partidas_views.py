from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ...models.presupuesto.partidas_presupuestarias import PartidasPresupuestarias

class ListarPartidas(ListView):
    model = PartidasPresupuestarias
    template_name = 'gestion_bodegas/presupuesto/listar_partidas.html'
    context_object_name = 'partidas'

    def get_queryset(self):
        return PartidasPresupuestarias.objects.filter(proyecto_id=self.kwargs['proyecto_id'])

class DetallePartida(DetailView):
    model = PartidasPresupuestarias
    template_name = 'gestion_bodegas/presupuesto/detalle_partida.html'
    context_object_name = 'partida'

class CrearPartida(CreateView):
    model = PartidasPresupuestarias
    template_name = 'gestion_bodegas/presupuesto/crear_partida.html'
    fields = ['nombre', 'descripcion', 'costo_estimado']

    def form_valid(self, form):
        form.instance.proyecto_id = self.kwargs['proyecto_id']
        form.instance.costo_real = 0.0  # Inicia en cero
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listar_partidas', kwargs={'proyecto_id': self.kwargs['proyecto_id']})

class EditarPartida(UpdateView):
    model = PartidasPresupuestarias
    template_name = 'gestion_bodegas/presupuesto/editar_partida.html'
    fields = ['nombre', 'descripcion', 'costo_estimado', 'costo_real']

    def get_success_url(self):
        return reverse_lazy('detalle_partida', kwargs={'pk': self.object.pk})

class EliminarPartida(DeleteView):
    model = PartidasPresupuestarias
    template_name = 'gestion_bodegas/presupuesto/eliminar_partida.html'

    def get_success_url(self):
        return reverse_lazy('listar_partidas', kwargs={'proyecto_id': self.object.proyecto_id})
