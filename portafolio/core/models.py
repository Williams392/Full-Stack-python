# 3

from django.db import models

class Proyecto:
    def __init__(self,nombre,descripcion,imagen, costo):
        self.nombre=nombre
        self.descripcion=descripcion
        self.imagen=imagen
        self.costo=costo

# instalar libreria para img en django: pip install pillow
class MiPortafolio(models. Model):
    proyecto = models.CharField(max_length=120)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="proyecto_img/", default="proyecto_img/img_2.jng")
    lenguaje = models.CharField(max_length=120)
    tecnologia = models.CharField(max_length=120, blank=True, null=True)
    año = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.proyecto
    
class Comentario(models. Model):
    comentario = models.TextField()
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre


# python manage.py makemigrations
# python manage.py migrate