from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.utils.translation import gettext_lazy as _


class UsuarioCriaForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'cpf',
            'idade',
            'endereco',
            'sexo',
            'pcd',
            'deficiencia',
        ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        cpf = cleaned_data.get('cpf')

        if Usuario.objects.filter(email=email).exists():
            self.add_error('email', 'Já existe um usuário com este email.')

        if Usuario.objects.filter(cpf=cpf).exists():
            self.add_error('cpf', 'Já existe um usuário com este CPF.')

        required_fields = ['username', 'email', 'first_name', 'last_name', 'cpf', 'idade', 'endereco', 'sexo']
        for field_name in required_fields:
            if not cleaned_data.get(field_name):
                self.add_error(field_name, f'O campo {self.fields[field_name].label} é obrigatório.')

        self.validate_idade(cleaned_data)
        self.validate_pcd_deficiencia(cleaned_data)

        return cleaned_data

    def validate_idade(self, cleaned_data):
        idade = cleaned_data.get('idade')
        if idade is not None:
            try:
                idade = int(idade)
                if idade < 0:
                    self.add_error('idade', 'A idade deve ser um número positivo.')
                elif idade < 18:
                    self.add_error('idade', 'Você deve ser maior de 18 anos para criar uma conta.')
            except ValueError:
                self.add_error('idade', 'A idade deve ser um número válido.')

    def validate_pcd_deficiencia(self, cleaned_data):
        pcd = cleaned_data.get('pcd')
        deficiencia = cleaned_data.get('deficiencia')

        if not pcd and deficiencia:
            self.add_error('deficiencia', "O campo 'Deficiência' não pode ser preenchido se o campo 'pcd' estiver marcado como falso.")

        if pcd and not deficiencia:
            self.add_error('deficiencia', "Deficiência é obrigatória para pessoas com deficiência.")


class UsuarioEditaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'cpf',
            'idade',
            'endereco',
            'sexo',
            'pcd',
            'deficiencia',
        ]

    def clean(self):
        cleaned_data = super().clean()

        self.validate_idade(cleaned_data)
        self.validate_pcd_deficiencia(cleaned_data)

        return cleaned_data

    def validate_idade(self, cleaned_data):
        idade = cleaned_data.get('idade')
        if idade is not None:
            try:
                idade = int(idade)
                if idade < 0:
                    self.add_error('idade', 'A idade deve ser um número positivo.')
                elif idade < 18:
                    self.add_error('idade', 'Você deve ser maior de 18 anos para criar uma conta.')
            except ValueError:
                self.add_error('idade', 'A idade deve ser um número válido.')

    def validate_pcd_deficiencia(self, cleaned_data):
        pcd = cleaned_data.get('pcd')
        deficiencia = cleaned_data.get('deficiencia')

        if not pcd and deficiencia:
            self.add_error('deficiencia', "O campo 'Deficiência' não pode ser preenchido se o campo 'pcd' estiver marcado como falso.")

        if pcd and not deficiencia:
            self.add_error('deficiencia', "Deficiência é obrigatória para pessoas com deficiência.")


class UsuarioRequeridEempresa(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('empresaRequiredPermission',)
        labels = {
            'empresaRequiredPermission': 'Solicitar permissão',
        }

class ConfirmarExclusaoForm(forms.Form):
     senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha para confirmar'}),
        label='Senha'
    )
