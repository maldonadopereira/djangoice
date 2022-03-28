from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telefone = models.CharField(max_length=15, default='')
    cep = models.CharField(max_length=10, default='')
    endereco = models.CharField(max_length=150, default='')
    foto_user = models.ImageField(upload_to='media/fotos/%d/%m/%Y', blank=True, default='', null=True)
