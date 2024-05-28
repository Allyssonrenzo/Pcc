from django.db import models
from django.core.exceptions import ValidationError
from usuario.models import Usuario  # Importe o modelo de Usuario corretamente

class Curriculo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)  
    telefone = models.CharField(max_length=30)
    formacao = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        """
        Create only one Curriculo instance per user
        """
        if not self.pk and Curriculo.objects.filter(usuario=self.usuario).exists():
            raise ValidationError(
                "Só é permitido criar um currículo por usuário."
            )
        return super(Curriculo, self).save(*args, **kwargs)
