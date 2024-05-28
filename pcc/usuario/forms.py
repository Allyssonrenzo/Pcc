from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


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

    def _init_(self, *args, **kwargs):
        super(UsuarioCriaForm, self)._init_(*args, **kwargs)
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação da Senha'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não correspondem.")
        
        # Validação de comprimento mínimo
        if len(password1) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        
        # Validação de complexidade (por exemplo, incluir números)
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("A senha deve incluir pelo menos um número.")
        
        return password2