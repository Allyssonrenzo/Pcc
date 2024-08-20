from django import forms
from .models import Entrevista
from usuario.models import Usuario
from empresa.models import Empresa
from candidatura.models import Candidatura
import datetime

class EntrevistaForm(forms.ModelForm):
    class Meta:
        model = Entrevista
        fields = ['data', 'hora', 'empresa', 'candidatura']

    def __init__(self, *args, **kwargs):
        super(EntrevistaForm, self).__init__(*args, **kwargs)
        self.fields['empresa'].queryset = Empresa.objects.all()
        self.fields['candidatura'].queryset = Candidatura.objects.all()
        self.fields['empresa'].widget = forms.HiddenInput()
        self.fields['candidatura'].widget = forms.HiddenInput()
        self.fields['data'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': datetime.date.today().strftime('%Y-%m-%d'), 'id': 'id_data'})
        
        self.fields['hora'].widget = forms.Select(choices=self.generate_time_choices())
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def generate_time_choices(self):
        times = []
        periods = [(7, 11, 30), (13, 17, 0)]
        for start_hour, end_hour, end_minute in periods:
            current_time = datetime.time(start_hour, 0)
            end_time = datetime.time(end_hour, end_minute)
            while current_time < end_time:
                times.append((current_time.strftime('%H:%M'), current_time.strftime('%H:%M')))
                current_time = (datetime.datetime.combine(datetime.date.today(), current_time) + datetime.timedelta(minutes=30)).time()
        return times

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data:
            if data < datetime.date.today():
                raise forms.ValidationError("A data não pode ser no passado.")
            if data.weekday() >= 5:
                raise forms.ValidationError("Selecione um dia da semana (Segunda a Sexta).")
        return data

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        hora = cleaned_data.get('hora')
        empresa = cleaned_data.get('empresa')

        if data and hora and empresa:
            if Entrevista.objects.filter(data=data, hora=hora, empresa=empresa).exists():
                self.add_error('hora', 'Já existe uma entrevista marcada para esta empresa neste horário.')

        return cleaned_data
