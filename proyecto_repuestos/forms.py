from django import forms
from .models import clientes  

class cliente_formulario(forms.ModelForm):
    class Meta:
        model = clientes  
        fields = ['nombre', 'apellido', 'email'] 
