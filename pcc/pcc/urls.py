from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from usuario import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('empresa/', include('empresa.urls')),
    path('vaga/', include('vaga.urls')),
    path('accounts/', include(urls)),
    path('curriculo/', include('curriculo.urls')),
    path('candidatura/', include('candidatura.urls')),
    path('entrevista/', include('entrevista.urls')),
    path('', usuario_views.home, name='home'),
]