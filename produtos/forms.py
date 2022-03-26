from django import forms

from produtos.models import Produto


class AdicionarProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome_produto', 'preco_produto', 'quantidade_produto', 'descricao_produto', 'disponivel', 'fornecedor'
        ]




