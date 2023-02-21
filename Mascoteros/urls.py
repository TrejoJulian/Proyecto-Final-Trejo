from django.contrib import admin
from django.urls import path, include
from Mascoteros.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('home/', home, name="Home"),
    path('register', register, name='Register'),
    path('login', login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='Mascoteros/Autenticar/logout.html'), name='Logout'),

    #CRUD ANIMALES
    path("animal/list/", ListaAnimal.as_view(), name="AnimalesLista"),
    path("animal/<int:pk>", DetalleAnimal.as_view(), name="AnimalesDetalle"),
    path("animal/crear/", CrearAnimal.as_view(), name="AnimalesCrear"),
    path("animal/editar/<int:pk>", ActualizarAnimal.as_view(), name="AnimalesEditar"),
    path("animal/borrar/<int:pk>", BorrarAnimal.as_view(), name="AnimalesBorrar"),

    path("resultadoAnimales/", resultado_animales, name="Resultado_Animales"),

    #CRUD Establecimientos
    path("establecimiento/list/", ListaEstablecimiento.as_view(), name="EstablecimientosLista"),
    path("establecimiento/<int:pk>", DetalleEstablecimiento.as_view(), name="EstablecimientosDetalle"),
    path("establecimiento/crear/", CrearEstablecimiento.as_view(), name="EstablecimientosCrear"),
    path("establecimiento/editar/<int:pk>", ActualizarEstablecimiento.as_view(), name="EstablecimientosEditar"),
    path("establecimiento/borrar/<int:pk>", BorrarEstablecimiento.as_view(), name="EstablecimientosBorrar"),

    path("resultadoEstablecimientos/", resultado_establecimientos, name="Resultado_Establecimientos"),

    #CRUD PRODUCTOS
    path("producto/list/", ListaProducto.as_view(), name="ProductosLista"),
    path("producto/<int:pk>", DetalleProducto.as_view(), name="ProductosDetalle"),
    path("producto/crear/", CrearProducto.as_view(), name="ProductosCrear"),
    path("producto/editar/<int:pk>", ActualizarProducto.as_view(), name="ProductosEditar"),
    path("producto/borrar/<int:pk>", BorrarProducto.as_view(), name="ProductosBorrar"),

    path("resultadoProductos/", resultado_productos, name="Resultado_Productos"),
]