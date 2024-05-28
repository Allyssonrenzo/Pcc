from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError



class Usuario(AbstractUser):

    cpf = models.CharField(max_length=30)
    idade = models.IntegerField(default=0)  
    endereco = models.CharField(max_length=150)
    sexo = models.CharField(max_length=20)
    pcd = models.BooleanField(default=False)
    deficiencia = models.CharField(max_length=100, blank=True)  
       

    def clean(self):
        cleaned_data = super().clean()

        if not self.pcd and self.deficiencia:
            raise ValidationError({"pcd": "O campo 'Deficiência' não pode ser preenchido se o campo 'pcd' estiver marcado como falso."})

        if self.pcd and not self.deficiencia:
            raise ValidationError({"deficiencia": "Deficiência é obrigatória para pessoas com deficiência."})

        return cleaned_data
    
   
        