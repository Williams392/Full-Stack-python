# 1

from django.shortcuts import render

def index(request):
    template_name = "index.html"
    return render(request, template_name)

def quienes(request):
    template_name = "quienessomos.html"
    return render(request, template_name)
