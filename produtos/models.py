from datetime import datetime
from django.db import models
from users.models import User
from clientes.models import Cliente
from localflavor.br.models import BRPostalCodeField, BRStateField, BRCNPJField

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=30, null=False)
    cnpj_fornecedor = BRCNPJField()
    endereco_fornecedor = models.CharField(max_length=150, null=False)
    cep_fornecedor = BRPostalCodeField()
    cidade_fornecedor = models.CharField(max_length=30, null=False)
    uf_fornecedor = BRStateField()
    telefone_fornecedor = models.CharField(max_length=15, null=False)
    email_fornecedor = models.EmailField(max_length=50, null=False)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome_fornecedor']

    def __str__(self):
        return self.nome_fornecedor

class Produto(models.Model):
    nome_produto = models.CharField(max_length=30, null=False )
    marca_produto = models.CharField(max_length=50, null=True)
    preco_produto = models.FloatField(null=False)
    quantidade_produto = models.IntegerField(default=0)
    descricao_produto= models.TextField(max_length=500, null=True)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, default='', on_delete=models.SET_NULL, null=True)
    fornecedor = models.ForeignKey(Fornecedor, default='', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome_produto


class Venda(models.Model):
    id_produto = models.ForeignKey(Produto, default='', on_delete=models.SET_NULL, null=True)
    id_user = models.ForeignKey(User, default='', on_delete=models.SET_NULL, null=True)
    id_cliente = models.ForeignKey(Cliente, default='', on_delete=models.SET_NULL, null=True)
    data_venda = models.DateTimeField(default=datetime.now, blank=True)
