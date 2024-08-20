from django import forms
from vaga.models import Vaga
from .models import Candidatura

class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ['vaga']

    def __init__(self, *args, **kwargs):
        vaga = kwargs.pop('vaga', None)
        super(CandidaturaForm, self).__init__(*args, **kwargs)
        if vaga:
            self.fields['vaga'].initial = vaga
            self.fields['vaga'].widget = forms.HiddenInput()
        else:
            self.fields['vaga'].queryset = Vaga.objects.all()