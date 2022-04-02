from django.shortcuts import render, get_object_or_404

from estoque.models import Estoque


def entrada_estoque_list(request):
    template_name = 'estoque/entrada_estoque_list.html'
    estoque = Estoque.objects.filter(movimento='e')
    context = {
        'estoque': estoque
    }


    return render(request, template_name, context)

def entrada_estoque_detail(request, estoque_id):
    estoque = get_object_or_404(Estoque, pk=estoque_id)
    context = {
        'estoque': estoque
    }
    template_name = 'estoque/entrada_estoque_detail.html'


    return render(request, template_name, context)

def entrada_estoque_add(request):
    template_name = 'estoque/entrada_estoque_detail.html'


    return render(request, 'estoque/entrada_estoque_add.html')





def saida_estoque(request):
    return render(request, 'estoque/saida_estoque.html')