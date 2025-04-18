from django.shortcuts import render, redirect, get_object_or_404
from ...models.bodega.inventario import InventarioBodega
from ...models.bodega.bodegas import Bodega
from ...models.bodega.articulos import Articulo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm
from ...models.bodega.ubicaciones import Zona, Estanteria, Nivel

class InventarioBodegaForm(ModelForm):
    class Meta:
        model = InventarioBodega
        fields = ['bodega', 'articulo', 'cantidad', 'zona', 'estanteria', 'nivel']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bodega'].queryset = Bodega.objects.all()
        self.fields['articulo'].queryset = Articulo.objects.all()
        self.fields['zona'].queryset = Zona.objects.all()
        self.fields['estanteria'].queryset = Estanteria.objects.all()
        self.fields['nivel'].queryset = Nivel.objects.all()
        self.fields['zona'].label = 'Zona (Opcional)'
        self.fields['estanteria'].label = 'Estantería (Opcional)'
        self.fields['nivel'].label = 'Nivel (Opcional)'
        self.fields['zona'].required = False
        self.fields['estanteria'].required = False
        self.fields['nivel'].required = False

class ListaInventario(ListView):
    model = InventarioBodega
    template_name = 'gestion_bodegas/inventario/lista_inventario.html'
    context_object_name = 'inventarios'

class CrearInventario(CreateView):
    model = InventarioBodega
    form_class = InventarioBodegaForm
    template_name = 'gestion_bodegas/inventario/crear_inventario.html'
    success_url = reverse_lazy('lista_inventario')

class EditarInventario(UpdateView):
    model = InventarioBodega
    form_class = InventarioBodegaForm
    template_name = 'gestion_bodegas/inventario/editar_inventario.html'
    success_url = reverse_lazy('lista_inventario')

class EliminarInventario(DeleteView):
    model = InventarioBodega
    template_name = 'gestion_bodegas/inventario/eliminar_inventario.html'
    success_url = reverse_lazy('lista_inventario')
    context_object_name = 'inventario_bodega'