from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('editar/', views.editar_perfil_usuario, name='editar_perfil_usuario'),
    path('perfil/', views.visualizar_perfil_usuario, name='visualizar_perfil_usuario'),
    path('aceitarUser/<int:user_id>/', views.aceitarUser, name='aceitarUser'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('tenhoInteresse/', views.tenhoInteresse, name='tenhoInteresse'),
    path("home/", views.home, name="home"),
    path("acessibilidade/", views.acessibilidade, name="acessibilidade")

]