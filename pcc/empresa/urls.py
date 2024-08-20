from django.urls import path
from .views import criar_empresa, editar_empresa, visualizar_perfil_empresa, excluir_empresa

urlpatterns = [
    path('criar/', criar_empresa, name='criar_empresa'),
    path('editar/<int:id_empresa>/', editar_empresa, name='editar_empresa'),
    path('perfil/', visualizar_perfil_empresa, name='visualizar_perfil_empresa'),
    path('excluir/', excluir_empresa, name='excluir_empresa'),
]
