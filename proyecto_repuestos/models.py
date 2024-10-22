from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class proveedores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

class sucursales(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)  

class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"