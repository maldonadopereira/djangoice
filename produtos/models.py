from datetime import datetime
from django.db import models
from users.models import User
from clientes.models import Cliente

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=30, null=False)
    cnpj_fornecedor = models.CharField(max_length=18, null=False)
    endereco_fornecedor = models.CharField(max_length=150, null=False)
    cep_fornecedor = models.CharField(max_length=10, default='')
    cidade_fornecedor = models.CharField(max_length=30, null=False)
    uf_fornecedor = models.CharField(max_length=2, null=False)
    telefone_fornecedor = models.CharField(max_length=15, null=False)
    email_fornecedor = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome_fornecedor

class Produto(models.Model):
    nome_produto = models.CharField(max_length=30, null=False )
    marca_produto = models.CharField(max_length=50, null=True)
    preco_produto = models.FloatField(null=False)
    quantidade_produto = models.IntegerField(default=0)
    descricao_produto= models.TextField(max_length=500)
    disponivel = models.BooleanField(default=False)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, default='', on_delete=models.SET_NULL, null=True)
    fornecedor = models.ForeignKey(Fornecedor, default='', on_delete=models.SET_NULL, null=True)
    #fornecedor = models.CharField(max_length=30, null=False )

    def __str__(self):
        return self.nome_produto


class Venda(models.Model):
    id_produto = models.ForeignKey(Produto, default='', on_delete=models.SET_NULL, null=True)
    id_user = models.ForeignKey(User, default='', on_delete=models.SET_NULL, null=True)
    id_cliente = models.ForeignKey(Cliente, default='', on_delete=models.SET_NULL, null=True)
    data_venda = models.DateTimeField(default=datetime.now, blank=True)
