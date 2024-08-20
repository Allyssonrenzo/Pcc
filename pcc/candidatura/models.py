from django.db import models
from usuario.models import Usuario
from vaga.models import Vaga

class Candidatura(models.Model):
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('reprovada', 'Reprovada'),
    ], default='pendente')
    data_candidatura = models.DateTimeField(auto_now_add=True)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    
    
    

    def __str__(self):
        return f"{self.usuario.username} - {self.vaga.funcao} - {self.status}"

    def empresa_nome(self):
        return self.vaga.empresa.nome

    def aprovar(self):
        self.status = 'aprovada'
        self.save()
        self.vaga.status = 'preenchida'
        self.vaga.save()

    def reprovar(self):
        self.status = 'reprovada'
        self.save()
