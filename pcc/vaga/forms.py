from django import forms
from .models import Vaga
from usuario.models import Usuario
from empresa.models import Empresa

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['funcao', 'requisitos', 'descricao', 'status', 'valorSalarial', 'cargaHoraria']

   

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VagaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        vaga = super(VagaForm, self).save(commit=False)
        if self.user:
            empresa = Empresa.objects.get(usuario=self.user)
            vaga.empresa = empresa
        if commit:
            vaga.save()
        return vaga
