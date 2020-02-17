from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario para registrar !!HAY QUE VERIFICAR SI ESTA BIEN EL CODIGO QUE SE UTILIZA PARA LA BASE DE DATOS!! -GERE-
class RegisterForm(UserCreationForm):
    primer_nombre = forms.CharField(empty_value="Primer Nombre")
    segundo_nombre = forms.CharField()
    primer_apellido = forms.CharField()
    segundo_apellido = forms.CharField()
    email = forms.EmailField()
    #Solo aceptar archivos de imagenes, investigar
    #foto_perfil = forms.ImageField()


class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]
