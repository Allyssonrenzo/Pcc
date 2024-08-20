from django.db import models
from usuario.models import User

class Empresa(models.Model):
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=30, unique=True)
    endereco = models.CharField(max_length=200)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
   
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
