from django.shortcuts import render, redirect, get_object_or_404
from ...models.bodega.bodegas import Bodega
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm

class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = ['nombre', 'ubicacion', 'descripcion']

class ListaBodegas(ListView):
    model = Bodega
    template_name = 'gestion_bodegas/bodegas/lista_bodegas.html'
    context_object_name = 'bodegas'

class CrearBodega(CreateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'gestion_bodegas/bodegas/crear_bodega.html'
    success_url = reverse_lazy('lista_bodegas')

class EditarBodega(UpdateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'gestion_bodegas/bodegas/editar_bodega.html'
    success_url = reverse_lazy('lista_bodegas')

class EliminarBodega(DeleteView):
    model = Bodega
    template_name = 'gestion_bodegas/bodegas/eliminar_bodega.html'
    success_url = reverse_lazy('lista_bodegas')
    context_object_name = 'bodega'