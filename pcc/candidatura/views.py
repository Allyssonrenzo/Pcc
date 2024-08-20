from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from empresa.models import Empresa
from vaga.views import has_empresa
from .models import Candidatura
from .forms import CandidaturaForm
from vaga.models import Vaga
from usuario.models import Usuario
from curriculo.models import Curriculo

@login_required
def ver_curriculo(request, candidatura_id):
    candidatura = get_object_or_404(Candidatura, pk=candidatura_id)
    usuario = candidatura.usuario
    curriculo = get_object_or_404(Curriculo, usuario=usuario)
    return render(request, 'candidatura/form_analise.html', {'curriculo': curriculo})

@login_required
def criar_candidatura(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)

    usuario = get_object_or_404(Usuario, username=request.user.username)

    if not Curriculo.objects.filter(usuario=usuario).exists():
        messages.error(request, 'Você deve ter um currículo cadastrado para se candidatar a uma vaga.')
        return redirect('listar_candidaturas')

    if Candidatura.objects.filter(usuario=usuario, vaga=vaga).exists():
        messages.error(request, 'Você já se candidatou para esta vaga.')
        return redirect('listar_candidaturas')

    if request.method == 'POST':
        form = CandidaturaForm(request.POST, vaga=vaga)
        if form.is_valid():
            candidatura = form.save(commit=False)
            candidatura.usuario = usuario  
            candidatura.vaga = vaga
            candidatura.save()
            return redirect('listar_candidaturas')
    else:
        form = CandidaturaForm(vaga=vaga)

    return render(request, 'candidatura/form_candidatura.html', {'form': form, 'vaga': vaga})

@login_required
def listar_candidaturas(request):
    usuario = get_object_or_404(Usuario, username=request.user.username)
    candidaturas = Candidatura.objects.filter(usuario=usuario)
    return render(request, 'candidatura/listar_candidaturas.html', {'candidaturas': candidaturas})

@login_required
def visualizar_candidaturas(request):
    if not has_empresa(request.user):
        return HttpResponseRedirect('/empresa/criar/?error=sem_empresa')
    
    empresa = get_object_or_404(Empresa, usuario=request.user)
    
    vagas = Vaga.objects.filter(empresa=empresa)
    
    candidaturas = Candidatura.objects.filter(vaga__in=vagas)
    
    return render(request, 'candidatura/candidaturas_recebidas.html', {'candidaturas': candidaturas})



@login_required
def excluir_candidatura(request, candidatura_id):
    candidatura = get_object_or_404(Candidatura, pk=candidatura_id)
    
  
    candidatura.delete()
    messages.success(request, 'Candidatura excluída com sucesso.')
    

    return redirect('listar_candidaturas')



@login_required
def vagas_disponiveis(request):
    usuario = request.user
    tem_curriculo = Curriculo.objects.filter(usuario=usuario).exists()
    vagas_disponiveis = Vaga.objects.all()
    
  
    vagas_candidatadas = list(Candidatura.objects.filter(usuario=usuario).values_list('vaga_id', flat=True))

    return render(request, 'candidatura/vagas_disponiveis.html', {
        'vagas_disponiveis': vagas_disponiveis,
        'tem_curriculo': tem_curriculo,
        'vagas_candidatadas': vagas_candidatadas
    })


@login_required
def aprovar_candidatura(request, candidatura_id):
    candidatura = get_object_or_404(Candidatura, pk=candidatura_id)

    if candidatura.vaga.empresa.usuario == request.user:
        candidatura.aprovar()
        messages.success(request, 'Candidato aprovado e vaga preenchida.')
    else:
        messages.error(request, 'Você não tem permissão para aprovar este candidato.')
    
    return redirect('visualizar_candidaturas')

@login_required
def reprovar_candidatura(request, candidatura_id):
    candidatura = get_object_or_404(Candidatura, pk=candidatura_id)

    if candidatura.vaga.empresa.usuario == request.user:
        candidatura.reprovar()
        messages.success(request, 'Candidato reprovado.')
    else:
        messages.error(request, 'Você não tem permissão para reprovar este candidato.')
    
    return redirect('visualizar_candidaturas')


