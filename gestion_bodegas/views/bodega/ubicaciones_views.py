from django.shortcuts import render, redirect, get_object_or_404
from ...models.bodega.ubicaciones import Zona, Estanteria, Nivel
from ...models.bodega.bodegas import Bodega
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm

# Vistas para Zona

class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields = ['nombre', 'bodega']

class ListaZonas(ListView):
    model = Zona
    template_name = 'gestion_bodegas/ubicaciones/zonas/lista_zonas.html'
    context_object_name = 'zonas'

class CrearZona(CreateView):
    model = Zona
    form_class = ZonaForm
    template_name = 'gestion_bodegas/ubicaciones/zonas/crear_zona.html'
    success_url = reverse_lazy('lista_zonas')

class EditarZona(UpdateView):
    model = Zona
    form_class = ZonaForm
    template_name = 'gestion_bodegas/ubicaciones/zonas/editar_zona.html'
    success_url = reverse_lazy('lista_zonas')
    context_object_name = 'zona'

class EliminarZona(DeleteView):
    model = Zona
    template_name = 'gestion_bodegas/ubicaciones/zonas/eliminar_zona.html'
    success_url = reverse_lazy('lista_zonas')
    context_object_name = 'zona'

# Vistas para Estanteria

class EstanteriaForm(ModelForm):
    class Meta:
        model = Estanteria
        fields = ['nombre', 'zona']

class ListaEstanterias(ListView):
    model = Estanteria
    template_name = 'gestion_bodegas/ubicaciones/estanterias/lista_estanterias.html'
    context_object_name = 'estanterias'

class CrearEstanteria(CreateView):
    model = Estanteria
    form_class = EstanteriaForm
    template_name = 'gestion_bodegas/ubicaciones/estanterias/crear_estanteria.html'
    success_url = reverse_lazy('lista_estanterias')

class EditarEstanteria(UpdateView):
    model = Estanteria
    form_class = EstanteriaForm
    template_name = 'gestion_bodegas/ubicaciones/estanterias/editar_estanteria.html'
    success_url = reverse_lazy('lista_estanterias')
    context_object_name = 'estanteria'

class EliminarEstanteria(DeleteView):
    model = Estanteria
    template_name = 'gestion_bodegas/ubicaciones/estanterias/eliminar_estanteria.html'
    success_url = reverse_lazy('lista_estanterias')
    context_object_name = 'estanteria'

# Vistas para Nivel

class NivelForm(ModelForm):
    class Meta:
        model = Nivel
        fields = ['nombre', 'estanteria']

class ListaNiveles(ListView):
    model = Nivel
    template_name = 'gestion_bodegas/ubicaciones/niveles/lista_niveles.html'
    context_object_name = 'niveles'

class CrearNivel(CreateView):
    model = Nivel
    form_class = NivelForm
    template_name = 'gestion_bodegas/ubicaciones/niveles/crear_nivel.html'
    success_url = reverse_lazy('lista_niveles')

class EditarNivel(UpdateView):
    model = Nivel
    form_class = NivelForm
    template_name = 'gestion_bodegas/ubicaciones/niveles/editar_nivel.html'
    success_url = reverse_lazy('lista_niveles')
    context_object_name = 'nivel'

class EliminarNivel(DeleteView):
    model = Nivel
    template_name = 'gestion_bodegas/ubicaciones/niveles/eliminar_nivel.html'
    success_url = reverse_lazy('lista_niveles')
    context_object_name = 'nivel'