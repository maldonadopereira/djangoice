from django import forms

from clientes.models import Cliente


class AdicionarCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome_cliente', 'telefone_cliente', 'cep_cliente', 'endereco_cliente', 'cpf_cliente'
        ]




