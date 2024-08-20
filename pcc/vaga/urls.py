from django.urls import path
from.import views

urlpatterns = [
    path('criar/', views.criar_vaga, name='criar_vaga'),
    path('listar/', views.listar_vagas, name='listar_vagas'),
    path('editar/<int:id_vaga>/', views.editar_vaga, name='editar_vaga'),
    path('deletar/<int:id_vaga>/', views.deletar_vaga, name='deletar_vaga'),
    path('deletar/confirmar/<int:id_vaga>/', views.confirmar_deletar_vaga, name='confirmar_deletar_vaga'),
]
