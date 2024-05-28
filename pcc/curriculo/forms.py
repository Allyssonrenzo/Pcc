from django.forms import ModelForm, HiddenInput
from django import forms
from curriculo.models import Curriculo
from usuario.models import Usuario

class CurriculoForm(ModelForm):
    
    nome = forms.CharField(label='Nome', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    idade = forms.IntegerField(label='Idade', required=False, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    cpf = forms.CharField(label='CPF', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    endereco = forms.CharField(label='Endereço', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    sexo = forms.CharField(label='Sexo', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    pcd = forms.BooleanField(label='PCD', required=False, widget=forms.CheckboxInput(attrs={'disabled': 'disabled'}))
    deficiencia = forms.CharField(label='Deficiência', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(CurriculoForm, self).__init__(*args, **kwargs)
        if user_id:
            usuario = Usuario.objects.filter(pk=user_id).first()
            if usuario:
                self.fields['usuario'].queryset = Usuario.objects.filter(pk=user_id)
                self.fields['usuario'].widget = HiddenInput()
                self.fields['usuario'].initial = user_id
                self.fields['usuario'].label = ''
                self.fields['nome'].initial = usuario.first_name
                self.fields['idade'].initial = usuario.idade
                self.fields['cpf'].initial = usuario.cpf
                self.fields['email'].initial = usuario.email
                self.fields['endereco'].initial = usuario.endereco
                self.fields['sexo'].initial = usuario.sexo
                self.fields['pcd'].initial = usuario.pcd
                self.fields['deficiencia'].initial = usuario.deficiencia

    class Meta:
        model = Curriculo
        fields = '__all__'