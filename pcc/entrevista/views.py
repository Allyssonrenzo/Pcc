from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Entrevista
from .forms import EntrevistaForm
from candidatura.models import Candidatura
from usuario.models import Usuario  

@login_required
def marcar_entrevista(request, candidatura_id):
    candidatura = get_object_or_404(Candidatura, pk=candidatura_id)
    empresa = candidatura.vaga.empresa
    usuario = candidatura.usuario

    if request.method == 'POST':
        form = EntrevistaForm(request.POST)
        if form.is_valid():
            entrevista = form.save(commit=False)          
            entrevista.usuario = usuario  
            entrevista.empresa = empresa
            entrevista.candidatura = candidatura
            entrevista.save()
            return redirect('listar_entrevistas')
    else:
        form = EntrevistaForm(initial={
            'usuario': usuario.id,
            'empresa': empresa.id,
            'candidatura': candidatura.id,
        })
    return render(request, 'entrevista/form_entrevista.html', {'form': form})

@login_required
def listar_entrevistas(request):
   
    usuario_autenticado = get_object_or_404(Usuario, id=request.user.id)

    if usuario_autenticado.groups.filter(name='Usuario').exists():
        entrevistas = Entrevista.objects.filter(candidatura__usuario=usuario_autenticado)
    elif usuario_autenticado.groups.filter(name='Empresa').exists():
        entrevistas = Entrevista.objects.filter(empresa=usuario_autenticado.empresa)
    else:
        entrevistas = Entrevista.objects.none()

    return render(request, 'entrevista/listar_entrevistas.html', {'entrevistas': entrevistas})



@login_required
def editar_entrevista(request, pk):
    entrevista = get_object_or_404(Entrevista, pk=pk)
    if request.method == 'POST':
        form = EntrevistaForm(request.POST, instance=entrevista)
        if form.is_valid():
            form.save()
            return redirect('listar_entrevistas')
    else:
        form = EntrevistaForm(instance=entrevista)
    return render(request, 'entrevista/form_entrevista.html', {'form': form})

@login_required
def excluir_entrevista(request, pk):
    entrevista = get_object_or_404(Entrevista, pk=pk)
    if request.method == 'POST':
        entrevista.delete()
        return redirect('listar_entrevistas')
    return render(request, 'entrevista/confirmar_exclusao.html', {'entrevista': entrevista})
