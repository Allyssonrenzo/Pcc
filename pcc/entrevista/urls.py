from django.urls import path
from .views import editar_entrevista, listar_entrevistas, marcar_entrevista, excluir_entrevista

urlpatterns = [
    path('editar/<int:pk>/', editar_entrevista, name='editar_entrevista'),
    path('listar/', listar_entrevistas, name='listar_entrevistas'),
    path('marcar/<int:candidatura_id>/', marcar_entrevista, name='marcar_entrevista'),
    path('excluir/<int:pk>/', excluir_entrevista, name='excluir_entrevista'),
]
