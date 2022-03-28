from django.db import models


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100, null=False)
    telefone_cliente = models.CharField(max_length=15, default='')
    cep_cliente = models.CharField(max_length=10, default='')
    endereco_cliente = models.CharField(max_length=150, default='')
    cpf_cliente = models.CharField(max_length=14, default='')

    def __str__(self):
        return self.nome_cliente
