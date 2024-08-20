from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    cpf = models.CharField(max_length=30)
    idade = models.IntegerField(default=0)
    endereco = models.CharField(max_length=150)
    sexo = models.CharField(max_length=20)
    deficiencia = models.CharField(max_length=100, blank=True)
    pcd = models.BooleanField(default=False)
    empresaRequiredPermission = models.BooleanField(default=False)
    empresaConfirmPermission = models.BooleanField(default=False)

   