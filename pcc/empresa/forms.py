from django import forms
from .models import Empresa

class EmpresaCriaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user', None)
        super(EmpresaCriaForm, self).__init__(*args, **kwargs)
        if user_id:
            self.fields['usuario'].initial = user_id
            self.fields['usuario'].disabled = True
            self.fields['usuario'].widget = forms.HiddenInput()
            self.fields['usuario'].label = ""
            
    def clean(self):
        cleaned_data = super().clean()
        cnpj = cleaned_data.get('cnpj')
        nome = cleaned_data.get('nome')

        if Empresa.objects.filter(cnpj=cnpj).exists():
            self.add_error('cnpj', 'Já existe uma empresa com este CNPJ.')

        if Empresa.objects.filter(nome=nome).exists():
            self.add_error('nome', 'Já existe uma empresa com este nome.')

        return cleaned_data


class EmpresaEditaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'telefone', 'endereco', 'email']

    def __init__(self, *args, **kwargs):
        super(EmpresaEditaForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        empresa_id = self.instance.id

        if Empresa.objects.filter(nome=nome).exclude(id=empresa_id).exists():
            self.add_error('nome', 'Já existe uma empresa com este nome.')

        return cleaned_data
