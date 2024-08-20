from django.db import models
from django.core.exceptions import ValidationError
from usuario.models import Usuario

class Curriculo(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    formacao = models.CharField(max_length=100, blank=True, null=True)
    experiencia = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"Currículo de {self.usuario}"
