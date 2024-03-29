from django.urls import path
from produtos import views

urlpatterns = [
    path('adicionar_produto', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:produto_id>', views.editar_produto, name='editar_produto'),
    path('listar_produto', views.listar_produto, name='listar_produto'),
    path('detalhar/<int:produto_id>', views.detalhar_produto, name='detalhar_produto'),
    path('buscar/', views.buscar, name='buscar'),
    path('adicionar_fornecedor', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('editar_fornecedor/<int:fornecedor_id>', views.editar_fornecedor, name='editar_fornecedor'),
    path('listar_fornecedor', views.listar_fornecedor, name='listar_fornecedor'),
    path('detalhar_fornecedor/<int:fornecedor_id>', views.detalhar_fornecedor, name='detalhar_fornecedor'),

    path('buscar_cep', views.buscar_cep, name='buscar_cep'),

]