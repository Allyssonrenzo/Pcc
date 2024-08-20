from django.urls import path
from . import views

urlpatterns = [
    path("criar/", views.criar, name="adicionar"),
    path("read/", views.listarTudo, name="ler"),
    path("editar/<int:id_curriculo>", views.editar, name="atualizar"),
    path("deletar/<int:id_curriculo>", views.deletar, name="deletar"),
    path("deletar/confirmar/<int:id_curriculo>", views.confirmarDelete, name="confirmar"),
    
]
