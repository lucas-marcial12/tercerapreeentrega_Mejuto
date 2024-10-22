from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import clientes
from .forms import cliente_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
        mi_formulario = cliente_formulario(req.POST)

        if mi_formulario.is_valid(): 
            data = mi_formulario.cleaned_data

            nuevo_cliente = clientes(nombre = data['nombre'], apellido = data['apellido'], email = data['email'])
            nuevo_cliente.save()
            return render(req, "inicio.html", {})
        else:
            return render(req, "clientes_formulario.html", {'mi_formulario': mi_formulario})

        
        

    else:
        mi_formulario = cliente_formulario()
        return render(req, "clientes_formulario.html", {'mi_formulario': mi_formulario})

def buscar_clientes(req):
    return render(req, "buscar_clientes.html", {})

def busqueda_clientes(req):

   
    mensaje = ''
    cliente = None
    
    if req.method == "GET":
        nombre_cliente = req.GET.get('cliente', None)
        
        if nombre_cliente:
            try:
                cliente = clientes.objects.get(nombre=nombre_cliente)
            except clientes.DoesNotExist:
                mensaje = f'No se encontró ningún cliente con el nombre "{nombre_cliente}".'
        else:
            mensaje = 'Por favor, introduce un nombre para buscar.'

    return render(req, "busqueda_clientes.html", {
        'cliente': cliente,
        'mensaje': mensaje})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                # Usar mensajes en lugar de pasar el mensaje directo al contexto
                messages.success(request, f"Bienvenido {usuario}")
                return redirect('inicio')  # Redireccionar en lugar de renderizar
            else:
                messages.error(request, "Error, datos incorrectos")
        else:
            messages.error(request, "Error, usuario invalido. Ingrese nuevamente su usuario y contraseña")

    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})
                
def registro(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"inicio.html", {"mensaje":" Usuario creado"})

    else:

        form = UserCreationForm()

    return render(request, "registro.html", {"form": form})    

def leerclientes(request):

      lista_clientes = clientes.objects.all() #trae todos los clientes

      contexto= {"clientes": lista_clientes} 

      return render(request, "leerclientes.html",contexto)

def eliminar_clientes(request, cliente_nombre):
 
    cliente = clientes.objects.get(nombre=cliente_nombre)
    cliente.delete()
 
    # vuelvo al menú
    clientes_eliminar = clientes.objects.all()  # trae todos los clientes
 
    contexto = {"clientes": clientes_eliminar}
 
    return render(request, "leerclientes.html", contexto)

def editar_clientes(request, cliente_id):
    cliente = get_object_or_404(clientes, id=cliente_id)  # Obtener el cliente por ID

    if request.method == "POST":
        mi_formulario = cliente_formulario(request.POST, instance=cliente)  # Cargar el formulario con los datos existentes

        if mi_formulario.is_valid():
            mi_formulario.save()  # Guardar los cambios
            return redirect('leerclientes')  # Redirigir a la lista de clientes después de editar
    else:
        mi_formulario = cliente_formulario(instance=cliente)  # Crear el formulario con los datos actuales

    contexto = {'mi_formulario': mi_formulario, 'cliente': cliente}
    return render(request, "editar_cliente.html", contexto)



def custom_logout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('inicio')

@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


class Cambiar_contrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiar_contrasenia.html'
    success_url = reverse_lazy('editar_perfil.html')