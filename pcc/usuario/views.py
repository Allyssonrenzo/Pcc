from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from usuario.forms import UsuarioCriaForm
from .models import Usuario
from django.contrib.auth.decorators import login_required


def criar(request):
     
    if request.method == 'POST':
        
        form = UsuarioCriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/?msg=Salvo')
        
    else:
        form = UsuarioCriaForm()

    return render(request, 'usuario/register.html', {'form': form})

@login_required
def editar_perfil(request):

    usuario = request.user
    
    if request.method == 'POST': 
        form = UsuarioEditaForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuario/perfil/?msg=Salvo') 
    else:
        form = UsuarioEditaForm(instance=usuario)
    
    return render(request, 'usuario/editar_perfil.html', {'form': form})


def visualizar_perfil(request):
    usuario = request.user
    return render(request, 'usuario/visualizarPerfil.html', {'usuario': usuario})