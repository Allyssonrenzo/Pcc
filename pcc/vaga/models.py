from django.db import models
from usuario.models import Usuario
from empresa.models import Empresa

class Vaga(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('preenchida', 'Preenchida')
    ]
    
    funcao = models.CharField(max_length=100)
    requisitos = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    valorSalarial = models.CharField(max_length=20)
    cargaHoraria = models.CharField(max_length=100)


    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcao
