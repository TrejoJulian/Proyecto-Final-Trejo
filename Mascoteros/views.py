from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Mascoteros.models import *
from Mascoteros.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request): 
    return render(request, "Mascoteros/home.html")

def about(request): 
    return render(request, "Mascoteros/about.html")


class ListaAnimal(ListView):

    model = Animal
    template_name = "Mascoteros/animal/animal_list.html"

class DetalleAnimal(DetailView):

    model = Animal
    template_name = "Mascoteros/animal/animal_detail.html"


class CrearAnimal(LoginRequiredMixin, CreateView):

    form_class = AnimalFormulario
    success_url = "/Mascoteros/animal/list"
    template_name = "Mascoteros/animal/animal_form.html"

class ActualizarAnimal(LoginRequiredMixin, UpdateView):
    model = Animal
    form_class = AnimalFormulario
    success_url = "/Mascoteros/animal/list"
    template_name = "Mascoteros/animal/animal_form.html"

class BorrarAnimal(LoginRequiredMixin, DeleteView):

    model = Animal
    success_url = "/Mascoteros/animal/list"
    template_name = "Mascoteros/animal/animal_confirm_delete.html"

class ListaEstablecimiento(ListView):

    model = Establecimiento
    template_name = "Mascoteros/establecimiento/establecimiento_list.html"

class DetalleEstablecimiento(DetailView):

    model = Establecimiento
    template_name = "Mascoteros/establecimiento/establecimiento_detail.html"

class CrearEstablecimiento(LoginRequiredMixin, CreateView):

    form_class = EstablecimientoFormulario
    success_url = "/Mascoteros/establecimiento/list"
    template_name = "Mascoteros/establecimiento/establecimiento_form.html"


class ActualizarEstablecimiento(LoginRequiredMixin, UpdateView):
    model = Establecimiento
    form_class = EstablecimientoFormulario
    success_url = "/Mascoteros/establecimiento/list"
    template_name = "Mascoteros/establecimiento/establecimiento_form.html"

class BorrarEstablecimiento(LoginRequiredMixin, DeleteView):

    model = Establecimiento
    success_url = "/Mascoteros/establecimiento/list"
    template_name = "Mascoteros/establecimiento/establecimiento_confirm_delete.html"


class ListaProducto(ListView):

    model = Producto
    template_name = "Mascoteros/producto/producto_list.html"

class DetalleProducto(DetailView):

    model = Producto
    template_name = "Mascoteros/producto/producto_detail.html"

class CrearProducto(LoginRequiredMixin, CreateView):

    form_class = ProductoFormulario
    success_url = "/Mascoteros/producto/list"
    template_name = "Mascoteros/producto/producto_form.html"



class ActualizarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoFormulario
    success_url = "/Mascoteros/producto/list"
    template_name = "Mascoteros/producto/producto_form.html"

class BorrarProducto(LoginRequiredMixin, DeleteView):

    model = Producto
    success_url = "/Mascoteros/producto/list"


def resultado_animales(request):

    animal_buscado = request.GET["nombre"]
    resultados_animales = Animal.objects.filter(nombre__icontains=animal_buscado)

    return render(request, "Mascoteros/animal/resultado_animal.html", {"nombre":animal_buscado, "animales": resultados_animales})


def resultado_establecimientos(request):

    establecimiento_buscado = request.GET["nombre"]
    resultados_establecimientos = Establecimiento.objects.filter(nombre__icontains=establecimiento_buscado)

    return render(request, "Mascoteros/establecimiento/resultado_establecimiento.html", {"nombre":establecimiento_buscado, "establecimientos": resultados_establecimientos})

def resultado_productos(request):

    producto_buscado = request.GET["nombre"]
    resultados_productos = Producto.objects.filter(nombre__icontains=producto_buscado)

    return render(request, "Mascoteros/producto/resultado_producto.html", {"nombre":producto_buscado, "productos": resultados_productos})


def register(request):

    if request.method == 'POST':   

        form = RegistroFormulario(request.POST)  

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "Mascoteros/home.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = RegistroFormulario()  
    
    
    return render(request, "Mascoteros/Autenticar/registro.html", {'form':form})



def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')  
            contra=form.cleaned_data.get('password')  

            user=authenticate(username=usuario, password=contra) 

            if user:

                login(request, user)

                return render(request, "Mascoteros/home.html") 

        else:
    
            return render(request, "Mascoteros/Autenticar/login.html", {'form':form, 'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm()

    return render(request, "Mascoteros/Autenticar/login.html", {'form':form})   
