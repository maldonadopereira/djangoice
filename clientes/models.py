from django.db import models
from localflavor.br.models import *


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100, null=False)
    telefone_cliente = models.CharField(max_length=15, default='')
    cep_cliente = BRPostalCodeField()
    endereco_cliente = models.CharField(max_length=150, default='')
    cpf_cliente = BRCPFField()

    def __str__(self):
        return self.nome_cliente
