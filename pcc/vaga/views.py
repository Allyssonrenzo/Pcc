from django import template
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from empresa.models import Empresa
from usuario.models import Usuario
from .forms import VagaForm
from .models import Vaga

register = template.Library()

@register.filter(name='has_group')
def has_group(user):
    return user.groups.filter(name="Empresa").exists()

def has_empresa(user):
    return Empresa.objects.filter(usuario=user).exists()

from django.shortcuts import get_object_or_404

@login_required
@user_passes_test(has_group)
def criar_vaga(request):
    if not has_empresa(request.user):
        return HttpResponseRedirect('/empresa/criar/?error=sem_empresa')

    if request.method == 'POST':
        form = VagaForm(request.POST, user=request.user)
        if form.is_valid():
            vaga = form.save(commit=False)
            usuario = get_object_or_404(Usuario, username=request.user.username)  
            vaga.usuario = usuario  
            vaga.save()
            return HttpResponseRedirect('/vaga/listar/')
        else:
            error_message = form.errors.as_json()
            return render(request, 'vaga/formVaga.html', {'form': form, 'error_message': error_message})
    else:
        form = VagaForm(user=request.user)

    return render(request, 'vaga/formVaga.html', {'form': form})

@login_required
def editar_vaga(request, id_vaga):
    vaga = get_object_or_404(Vaga, pk=id_vaga)

    if vaga.empresa.usuario != request.user:
        return HttpResponseRedirect('/vaga/listar/?error=sem_permissao')

    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.save()
            return HttpResponseRedirect('/vaga/listar/')
        else:
            print(form.errors)  
    else:
        form = VagaForm(instance=vaga)
    
    return render(request, 'vaga/updateVaga.html', {'form': form, 'id_vaga': id_vaga})


@login_required
def listar_vagas(request):
    if not has_empresa(request.user):
        return HttpResponseRedirect('/empresa/criar/?error=sem_empresa')
    
    vagas_empresa = Vaga.objects.filter(empresa__usuario=request.user)
    return render(request, 'vaga/listarTudo.html', {'vagas': vagas_empresa})
    
    

@login_required
def deletar_vaga(request, id_vaga):
    vaga = get_object_or_404(Vaga, pk=id_vaga)
    vaga.delete()
    return HttpResponseRedirect('/vaga/listar/')

@login_required
def confirmar_deletar_vaga(request, id_vaga):
    vaga = get_object_or_404(Vaga, pk=id_vaga)
    return render(request, 'vaga/confirmarExcluir.html', {'vaga': vaga})
