# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
#Se tendria que trabajar en una respuesta de verificacion de usuario creado -GERE-
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        #Si el formulario es correcto se guarda
        if form.is_valid():
            form.save()
    else:
            form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

#Renderiza afterlogin.html luego de hacer login !!TEMPORAL!! -GERE-
def afterlogin(request):
    return render(request, "afterlogin.html")

#Renderiza afterlogout.html luego de hacer logout !!TEMPORAL!! -GERE-
def afterlogout(request):
    return render(request, "afterlogout.html")
