from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from vaga.views import has_empresa
from .forms import EmpresaCriaForm, EmpresaEditaForm
from .models import Empresa

def is_usuario(user):
    return user.groups.filter(name='Usuario').exists()

def is_empresa(user):
    return user.groups.filter(name='Empresa').exists()

@login_required
@user_passes_test(is_empresa)
def editar_empresa(request, id_empresa):
    empresa = get_object_or_404(Empresa, id=id_empresa, usuario=request.user)

    if request.method == 'POST':
        form = EmpresaEditaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/empresa/perfil?msg=Salvo')

    else:
        form = EmpresaEditaForm(instance=empresa)

    return render(request, 'empresa/editarEmpresa.html', {'form': form, 'empresa': empresa})



@login_required
@user_passes_test(is_empresa)
def excluir_empresa(request):
    empresa = get_object_or_404(Empresa, usuario=request.user)
    if request.method == 'POST':
        empresa.delete()
        return HttpResponseRedirect('/usuario/home/?msg=Empresa excluída com sucesso.')

    return render(request, 'empresa/excluir_empresa.html', {'empresa': empresa})

@login_required
@user_passes_test(is_empresa)
def criar_empresa(request):
    if request.method == 'POST':
        form = EmpresaCriaForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuario/home/?msg=Salvo')
        else:
            print(form.errors)  
    else:
        form = EmpresaCriaForm(user=request.user)

    return render(request, 'empresa/register.html', {'form': form})



@login_required
@user_passes_test(is_empresa)
def visualizar_perfil_empresa(request):
    if not has_empresa(request.user):
        return HttpResponseRedirect('/empresa/criar/?error=sem_empresa')
    
    empresa = get_object_or_404(Empresa, usuario=request.user)
    return render(request, 'empresa/visualizar_perfil.html', {'empresa': empresa})

