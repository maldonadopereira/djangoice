from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from .forms import AdicionarCliente
from .models import Cliente

def adicionar_cliente(request):
    if not request.user.has_perm('global_permissions.manipular_produto'):
        raise PermissionDenied
    else:
        if request.method == 'POST':
            form = AdicionarCliente(request.POST)
            if form.is_valid():
                produto = form.save()
                form = AdicionarCliente()
            context = {
                'form': form
            }
            return render(request, 'clientes/adicionar_cliente.html', context=context)

        else:
            form = AdicionarCliente()
            context = {
                'form': form
            }
            return render(request, 'clientes/adicionar_cliente.html', context=context)


def listar_cliente(request):
    if request.user.is_authenticated:
        clientes = Cliente.objects.order_by('id')
        dados = {
            'clientes': clientes
        }
        return render(request, 'clientes/listar_cliente.html', dados)
