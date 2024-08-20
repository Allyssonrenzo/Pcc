from django import forms
from .models import Curriculo
from django.forms.widgets import HiddenInput

class CurriculoForm(forms.ModelForm):

    class Meta:
        model = Curriculo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(CurriculoForm, self).__init__(*args, **kwargs)
        if user_id:
            self.fields['usuario'].initial = user_id
            self.fields['usuario'].disabled = True
            self.fields['usuario'].widget = HiddenInput()
            self.fields['usuario'].label = ""