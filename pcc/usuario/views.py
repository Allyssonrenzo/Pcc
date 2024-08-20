from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UsuarioCriaForm, UsuarioEditaForm, UsuarioRequeridEempresa, ConfirmarExclusaoForm
from django.contrib.auth.models import Group
from .models import Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import logout



def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def aceitarUser(request, user_id):
    if request.method == 'POST':

        try:
            novo_grupo = Group.objects.get(name='Empresa')
        except:
            novo_grupo = Group.objects.create(name = "Empresa")
            
        usuario = get_object_or_404(Usuario, id=user_id)
        usuario.groups.clear()
        usuario.groups.add(novo_grupo)
        usuario.empresaRequiredPermission = True
        usuario.empresaConfirmPermission = True

        usuario.save()

        return HttpResponseRedirect('/usuario/listar_usuarios/')

@user_passes_test(is_admin)
def listar_usuarios(request):
    usuarios = Usuario.objects.filter(empresaRequiredPermission=True, empresaConfirmPermission=False)
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioCriaForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                grupo_usuario = Group.objects.get(name='Usuario')
            except:
                grupo_usuario = Group.objects.create(
                    name = "Usuario"
                )

            user.groups.add(grupo_usuario)
            user.save()
            return HttpResponseRedirect('/accounts/login/?msg=Salvo')
    else:
        form = UsuarioCriaForm()

    return render(request, 'usuario/register.html', {'form': form})

@login_required
def editar_perfil_usuario(request):
    usuario = get_object_or_404(Usuario, id=request.user.id)  
    if request.method == 'POST': 
        form = UsuarioEditaForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuario/perfil/?msg=Salvo')
    else:
        form = UsuarioEditaForm(instance=usuario)
    
    return render(request, 'usuario/editar_perfil.html', {'form': form})

@login_required
def visualizar_perfil_usuario(request):
    usuario = get_object_or_404(Usuario, id=request.user.id)  

    if request.method == 'POST':
        form = ConfirmarExclusaoForm(request.POST)
        if form.is_valid():
            senha = form.cleaned_data['senha']
            if request.user.check_password(senha):
                request.user.delete()
                logout(request)  
                return redirect('/accounts/login/?msg=Conta excluída com sucesso.')
            else:
                form.add_error('senha', 'Senha incorreta. Tente novamente.')
    else:
        form = ConfirmarExclusaoForm()
   
    return render(request, 'usuario/visualizarPerfil.html', {'usuario': usuario, 'form': form})

@login_required
def tenhoInteresse(request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=request.user.id)
        form = UsuarioRequeridEempresa(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuario/home/')
        else:
            print("Form errors:", form.errors)


def home(request):
    form = UsuarioRequeridEempresa()
    try:
        user = Usuario.objects.get(id=request.user.id)
    except Usuario.DoesNotExist:
        user = request.user

    return render(request, 'homepage.html', {'form': form, 'user': user})
    
@login_required
def acessibilidade(request):
    form = UsuarioRequeridEempresa()
    try:
        user = Usuario.objects.get(id=request.user.id)
    except Usuario.DoesNotExist:
        user = request.user

    return render(request, 'acessibilidade.html', {'form': form, 'user': user})
