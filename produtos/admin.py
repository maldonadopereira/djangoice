from django.contrib import admin
from .models import Produto, Fornecedor


class ListandoProduto(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'preco_produto','fornecedor' ,'disponivel')
    list_display_links = ('id', 'nome_produto')
    search_fields = ('nome_receita',)
    list_filter = ('disponivel',)
    list_editable = ('disponivel',)
    list_per_page = 20

class ListandoFornecedor(admin.ModelAdmin):
    list_display = ('id', 'nome_fornecedor', 'telefone_fornecedor')
    list_display_links = ('id', 'nome_fornecedor')
    search_fields = ('nome_fornecedor',)
    list_per_page = 20

admin.site.register(Produto, ListandoProduto,)
admin.site.register(Fornecedor, ListandoFornecedor,)



