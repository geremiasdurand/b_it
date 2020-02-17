"""alojamientos_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
#Se importan las views de register como "rv" para no confundir
from register import views as rv

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", views.inicio),
    path("", views.inicio),
    path("register/", rv.register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("afterlogin/", rv.afterlogin, name="Solo por ahora, luego se edita"),
    path("afterlogout/", rv.afterlogout, name="Solo por ahora, luego se edita"),
]
