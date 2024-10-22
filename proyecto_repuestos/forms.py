from django import forms
from .models import clientes 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class cliente_formulario(forms.ModelForm):
    class Meta:
        model = clientes  
        fields = ['nombre', 'apellido', 'email'] 

class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):

    #Especificar los campos
    
    imagen = forms.ImageField(required=True)