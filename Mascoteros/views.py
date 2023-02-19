from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Mascoteros.models import *

# Create your views here.

def home(request): 
    return render(request, "Mascoteros/home.html")



class ListaAnimal(ListView):

    model = Animal
    template_name = "Mascoteros/animal/animal_list.html"

class DetalleAnimal(DetailView):

    model = Animal
    template_name = "Mascoteros/animal/animal_detail.html"

class CrearAnimal(CreateView):

    model = Animal
    success_url = "Mascoteros/animal/animal_list.html"
    template_name = "Mascoteros/animal/animal_form.html"
    fields = ["especie", "nombre", "descripcion", "imagen", "tamaño", "apto_niños"]

class ActualizarAnimal(UpdateView):
    model = Animal
    success_url = "Mascoteros/animal/animal_list.html"
    template_name = "Mascoteros/animal/animal_form.html"
    fields = ["especie", "nombre", "descripcion", "imagen", "tamaño", "apto_niños"]

class BorrarAnimal(DeleteView):

    model = Animal
    success_url = "Mascoteros/animal/animal_list.html"
    template_name = "Mascoteros/animal/animal_confirm_delete.html"

class ListaEstablecimiento(ListView):

    model = Establecimiento
    template_name = "Mascoteros/establecimiento/establecimiento_list.html"

class DetalleEstablecimiento(DetailView):

    model = Establecimiento
    template_name = "Mascoteros/establecimiento/establecimiento_detail.html"

class CrearEstablecimiento(CreateView):

    model = Establecimiento
    success_url = "Mascoteros/establecimiento/establecimiento_list.html"
    template_name = "Mascoteros/establecimiento/establecimiento_form.html"
    fields = ["nombre", "direccion", "horario", "imagen", "descripcion", "pagina_web"]


class ActualizarEstablecimiento(UpdateView):
    model = Establecimiento
    success_url = "Mascoteros/establecimiento/establecimiento_list.html"
    template_name = "Mascoteros/establecimiento/establecimiento_form.html"
    fields = ["nombre", "direccion", "horario", "imagen", "descripcion", "pagina_web"]

class BorrarEstablecimiento(DeleteView):

    model = Establecimiento
    success_url = "Mascoteros/establecimiento/establecimiento_list.html"
    template_name = "Mascoteros/establecimiento/establecimiento_confirm_delete.html"


class ListaProducto(ListView):

    model = Producto
    template_name = "Mascoteros/producto/producto_list.html"

class DetalleProducto(DetailView):

    model = Producto
    template_name = "Mascoteros/producto/producto_detail.html"

class CrearProducto(CreateView):

    model = Producto
    success_url = "Mascoteros/producto/producto_list.html"
    template_name = "Mascoteros/producto/producto_form.html"
    fields = ["nombre", "descripcion", "imagen", "especie_objetivo", "tipo"]



class ActualizarProducto(UpdateView):
    model = Producto
    success_url = "Mascoteros/producto/producto_list.html"
    template_name = "Mascoteros/producto/producto_form.html"
    fields = ["nombre", "descripcion", "imagen", "especie_objetivo", "tipo"]

class BorrarProducto(DeleteView):

    model = Producto
    success_url = "Mascoteros/producto/producto_list.html"
    success_url = "Mascoteros/producto/producto_list.html"
