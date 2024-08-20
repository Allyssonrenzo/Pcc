from django.urls import path
from .views import criar_candidatura, listar_candidaturas, aprovar_candidatura, excluir_candidatura, vagas_disponiveis, visualizar_candidaturas, reprovar_candidatura, ver_curriculo

urlpatterns = [
    path('criar/<int:vaga_id>/', criar_candidatura, name='criar_candidatura'),
    path('listar/', listar_candidaturas, name='listar_candidaturas'),
    path('aprovar/<int:candidatura_id>/', aprovar_candidatura, name='aprovar_candidatura'),
    path('reprovar/<int:candidatura_id>/', reprovar_candidatura, name='reprovar_candidatura'),
    path('excluir/<int:candidatura_id>/', excluir_candidatura, name='excluir_candidatura'),
    path('visualizar/', visualizar_candidaturas, name='visualizar_candidaturas'),
    path('vagas/', vagas_disponiveis, name='vagas_disponiveis'),
    path('ver_curriculo/<int:candidatura_id>/', ver_curriculo, name='ver_curriculo'),  
]