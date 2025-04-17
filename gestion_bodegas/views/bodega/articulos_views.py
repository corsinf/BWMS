from django.shortcuts import render, redirect, get_object_or_404
from ...models.bodega.articulos import Articulo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['codigo_rfid', 'nombre', 'descripcion', 'categoria']

class ListaArticulos(ListView):
    model = Articulo
    template_name = 'gestion_bodegas/articulos/lista_articulos.html'
    context_object_name = 'articulos'

class CrearArticulo(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'gestion_bodegas/articulos/crear_articulo.html'
    success_url = reverse_lazy('lista_articulos')

class EditarArticulo(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'gestion_bodegas/articulos/editar_articulo.html'
    success_url = reverse_lazy('lista_articulos')

class EliminarArticulo(DeleteView):
    model = Articulo
    template_name = 'gestion_bodegas/articulos/eliminar_articulo.html'
    success_url = reverse_lazy('lista_articulos')
    context_object_name = 'articulo'