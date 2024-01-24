# 2

from django.urls import path
from .views import index, quienes

urlpatterns = [
    path('', index),
    path('quienes/', quienes),
]