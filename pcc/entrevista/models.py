from django.db import models
from empresa.models import Empresa
from candidatura.models import Candidatura

class Entrevista(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    candidatura = models.OneToOneField(Candidatura, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Entrevista de {self.candidatura.usuario} com {self.empresa} em {self.data} às {self.hora}"

