from validate_docbr import CNPJ
from django.core.exceptions import ValidationError

def cnpj_valido(numero_cnpj):
    cnpj = CNPJ()
    return cnpj.validate(numero_cnpj)

def nome_valido(nome):
    return nome.isalpha()
