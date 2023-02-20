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



#Vista para registrarse
def register(request):

    if request.method == 'POST':    #cuando le haga click al botón

        form = RegistroFormulario(request.POST)   #leer los datos   llenados en el formulario

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "Mascoteros/home.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = RegistroFormulario()   #formulario de django que nos permite crear usuarios.
    
    
    return render(request, "Mascoteros/Autenticar/registro.html", {'form':form})



#Vista para iniciar sesión
def login_request(request):

    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"

        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contra=form.cleaned_data.get('password')    #leer la contraseña ingresada

            user=authenticate(username=usuario, password=contra)    #buscar al usuario con los datos ingresados

            if user:    #si ha encontrado un usuario con eso datos

                login(request, user)   #hacemos login

                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "Mascoteros/home.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   #si el formulario no es valido (no encuentra usuario)

            #mostramos la página de inicio junto a un mensaje de error.
    
            return render(request, "Mascoteros/home.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "Mascoteros/Autenticar/login.html", {'form':form})    #vincular la vista con la plantilla de html
