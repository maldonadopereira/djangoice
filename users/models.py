from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRPostalCodeField, BRStateField


class User(AbstractUser):
    telefone = models.CharField(max_length=15, default='')
    cep = BRPostalCodeField()
    endereco = models.CharField(max_length=150, default='')
    uf = BRStateField(null=True, default='')
    foto_user = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True, default='')
