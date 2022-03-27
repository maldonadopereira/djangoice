from django.urls import path
from produtos import views

urlpatterns = [
    path('adicionar_produto', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:produto_id>', views.editar_produto, name='editar_produto'),
    path('listar_produto', views.listar_produto, name='listar_produto'),
    path('detalhar/<int:produto_id>', views.detalhar_produto, name='detalhar_produto'),
]