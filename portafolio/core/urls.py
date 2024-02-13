# 2

from django.urls import path
from .views import index, detalles

urlpatterns = [
    path('', index, name="index"),
    path('detalle/<int:id>', detalles, name="detalle"),
]