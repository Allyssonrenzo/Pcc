from django.urls import path
from . import views

urlpatterns = [
    path("criar/", views.criar, name="adicionar"),
    path("editar/", views.editar_perfil, name="editar"),
    path('perfil/', views.visualizar_perfil, name='perfil'),
]