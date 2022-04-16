from django import forms
from produtos.models import Produto, Fornecedor


class AdicionarProduto(forms.ModelForm):

    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedor.objects.all(),
        label='Fornecedor',
        widget=forms.Select,
    )
    class Meta:
        model = Produto
        fields = [
            'nome_produto', 'marca_produto', 'preco_produto', 'quantidade_produto', 'descricao_produto',
        ]



class AdicionarFornecedor(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nome_fornecedor', 'cnpj_fornecedor', 'endereco_fornecedor', 'cep_fornecedor',
            'cidade_fornecedor', 'uf_fornecedor', 'telefone_fornecedor', 'email_fornecedor',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



