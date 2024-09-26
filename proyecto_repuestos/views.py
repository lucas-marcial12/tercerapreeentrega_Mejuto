from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import clientes
from .forms import cliente_formulario
# Create your views here.

# Create your views here.
def registra_cliente(req, nombre, apellido, email):
    nuevo_cliente = clientes(nombre = nombre, apellido = apellido, email = email)
    nuevo_cliente.save()

    return HttpResponse(f"""
        <p> Nombre: {nuevo_cliente.nombre} - Apellido: {nuevo_cliente.apellido} creado con exito</p>              
                        
                        
                     """)

def lista_clientes(req):
    lista = clientes.objects.all()

    return render(req, 'lista_clientes.html', {'lista_clientes': lista})

def inicio(req):

    return render(req, "inicio.html", {})

def proveedores(req):

    return render(req, "proveedores.html", {})

def sucursales(req):

    return render(req, "sucursales.html", {})

def quienes_somos(req):

    return render(req, "quienes_somos.html", {})

def clientes_formulario(req):
    
    print('method', req.method)
    print('data', req.POST)

    if req.method == "POST":
        nuevo_cliente = clientes(nombre = req.POST['nombre'], apellido = req.POST['apellido'], email = req.POST['email'])
        nuevo_cliente.save()
        return render(req, "inicio.html", {})

    else:
        mi_formulario = cliente_formulario()
    return render(req, "clientes_formulario.html", {'mi_formulario': mi_formulario})