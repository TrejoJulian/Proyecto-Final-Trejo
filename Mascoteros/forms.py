from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Se crean estas variables para definir los valores de los campos de tipo dropdown
opciones_especie = [
    ("Perro","Perro"),
    ("Gato","Gato")
]

opciones_tipo_producto = [
    ("Paseo","Paseo"),
    ("Juguete","Juguete"),
    ("Alimento", "Alimento"),
    ("Cosmético", "Cosmético")
]
opciones_tamaño = [
    ("Toy","Toy"),
    ("Pequeño","Pequeño"),
    ("Mediano","Mediano"),
    ("Grande","Grande"),
    ("Gigante","Gigante")
]

opciones_apto_niños = [
    ("True","Si"),
    ("False","No")
]


class AnimalFormulario(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ("especie", "nombre", "descripcion", "imagen", "tamaño", "apto_niños")

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.Select(choices=opciones_especie),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'tamaño':  forms.Select(choices=opciones_tamaño),
            'apto_niños': forms.Select(choices=opciones_apto_niños)
        }

class EstablecimientoFormulario(forms.ModelForm):

    class Meta:
        model = Establecimiento
        fields = ("nombre", "direccion", "horario", "imagen", "descripcion", "pagina_web")

        widgets = {
            'descripcion': forms.Textarea,
        }

class ProductoFormulario(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ("nombre", "descripcion", "imagen", "especie_objetivo", "tipo")

        widgets = {
            'especie_objetivo': forms.Select(choices=opciones_especie),
            'descripcion': forms.Textarea,
            'tipo': forms.Select(choices=opciones_tipo_producto)
        }


class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}