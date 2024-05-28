from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from curriculo.forms import CurriculoForm
from django.contrib.auth.decorators import login_required

from .models import Curriculo

@login_required
def criar(request):
     
    if request.method == 'POST':
        
        form = CurriculoForm(request.POST, user_id=request.user.id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../../curriculo/read/?msg=Salvo')
        
    else:
        form = CurriculoForm(user_id=request.user.id)
    
    return render(request, 'curriculo/formCurriculo.html', {'form': form})

@login_required
def listarTudo(request):

        curriculos = Curriculo.objects.filter(usuario=request.user)
        return render(request, 'curriculo/listarTudo.html', {'curriculo': curriculos})

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
    
    return render(request, 'curriculo/updateCurriculo.html', {'form': form, 'id_curriculo' : id_curriculo})

@login_required
def deletar(request, id_curriculo):
    
    curriculo = Curriculo.objects.get(pk=id_curriculo)
    curriculo.delete()
    return HttpResponseRedirect('../../curriculo/read/?msg=Apagado')

@login_required
def confirmarDelete(request, id_curriculo):
    
   curriculo = Curriculo.objects.get(pk=id_curriculo)    

   return render(request, 'curriculo/confirmarExcluir.html', {'curriculo': curriculo})

@login_required
def detail(request, id_curriculo):

    try:
        saida = Curriculo.objects.get(pk=id_curriculo)

    except Curriculo.DoesNotExist:
        saida = "Aqui não tem curriculo" 

    return render(request, 'curriculo/index.html', {'curriculo': saida})


def home(request):

    curriculos = Curriculo.objects.all()

    return render(request, 'homepage.html', {'curriculo': curriculos})