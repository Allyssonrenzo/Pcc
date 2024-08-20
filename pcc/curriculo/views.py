from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from usuario.forms import UsuarioRequeridEempresa
from usuario.models import Usuario
from .forms import CurriculoForm
from .models import Curriculo

@login_required
def criar(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST, user_id=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('ler')
        else:
            print(form.errors)
    else:
        form = CurriculoForm(user_id=request.user.id)

    return render(request, 'curriculo/formCurriculo.html', {'form': form})

@login_required
def editar(request, id_curriculo):
    curriculo = Curriculo.objects.get(pk=id_curriculo)

    if request.method == 'POST':
        form = CurriculoForm(request.POST, instance=curriculo, user_id=curriculo.usuario_id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../../curriculo/read/?msg=Salvo')
    else:
        form = CurriculoForm(instance=curriculo, user_id=curriculo.usuario_id)

    return render(request, 'curriculo/updateCurriculo.html', {'form': form, 'id_curriculo': id_curriculo})

@login_required
def listarTudo(request):
    tem_curriculo = Curriculo.objects.filter(usuario=request.user).exists()
    
    if not tem_curriculo:
        return redirect('adicionar')
    
    curriculos = Curriculo.objects.filter(usuario=request.user)
    return render(request, 'curriculo/listarTudo.html', {'curriculo': curriculos, 'tem_curriculo': tem_curriculo})

@login_required
def deletar(request, id_curriculo):
    curriculo = Curriculo.objects.get(pk=id_curriculo)
    curriculo.delete()
    return HttpResponseRedirect('../../curriculo/criar/?msg=Apagado')

@login_required
def confirmarDelete(request, id_curriculo):
    curriculo = Curriculo.objects.get(pk=id_curriculo)
    return render(request, 'curriculo/confirmarExcluir.html', {'curriculo': curriculo})

