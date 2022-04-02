from django.contrib import admin
from .models import Produto, Fornecedor

@admin.register(Produto)
class ListandoProduto(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'preco_produto','fornecedor', 'quantidade_produto')
    list_display_links = ('id', 'nome_produto')
    search_fields = ('nome_produto',)
    list_per_page = 20




@admin.register(Fornecedor)
class ListandoFornecedor(admin.ModelAdmin):
    list_display = ('id', 'nome_fornecedor', 'telefone_fornecedor')
    list_display_links = ('id', 'nome_fornecedor')
    search_fields = ('nome_fornecedor',)
    list_per_page = 20



