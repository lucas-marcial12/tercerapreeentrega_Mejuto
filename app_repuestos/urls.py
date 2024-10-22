"""
URL configuration for app_repuestos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from proyecto_repuestos.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name= 'inicio'),
    path('lista_clientes/', lista_clientes, name= 'lista_clientes'),
    path('proveedores/', proveedores, name= 'proveedores'),
    path('sucursales/', sucursales, name= 'sucursales'),
    path('quienes_somos/', quienes_somos, name= 'quienes_somos'),
    path('clientes_formulario/', clientes_formulario, name= 'clientes_formulario'),
    path('buscar_clientes/', buscar_clientes, name= 'buscar_clientes'),
    path('busqueda_clientes/', busqueda_clientes, name= 'busqueda_clientes'),
    path('login/', login_request, name= 'login'),
    path('registro/', registro, name='registro'),
    path('logout/', custom_logout, name='logout'),

    path('leerclientes/', leerclientes, name='leerclientes'),
    path('eliminar_clientes/<cliente_nombre>/', eliminar_clientes, name="eliminar_clientes"),
    path('editar_clientes/<int:cliente_id>/', editar_clientes, name="editar_clientes"),
    path('editar_perfil', editarPerfil, name="editar_perfil"), 
    path('cambiar_contrasenia', Cambiar_contrasenia.as_view(), name="cambiar_contrasenia"), 



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)