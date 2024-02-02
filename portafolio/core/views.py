# 1

from django.shortcuts import render
from .models import Proyecto, MiPortafolio

def index(request):
    template_name = "index.html"

    # Lista:
    # proyectos = [
    #     Proyecto("Proyecto1", "Descripcion del Proyecto 1", "img_1.jpeg", 120),
    #     Proyecto("Proyecto2", "Descripcion del Proyecto 2", "img_2.png", 180),
    #     Proyecto("Proyecto3", "Descripcion del Proyecto 3", "img_1.jpeg", 200),
    #     Proyecto("Proyecto4", "Descripcion del Proyecto 4", "img_2.png", 140)
    #     # agregar mas proyectos segun sea necesario
    # ]

    miportafolio = MiPortafolio.objects.all() # select * fromn MiPortafolio

    context = { # para pasar al templates
        'proyectos':miportafolio
    }

    return render(request, template_name, context)


