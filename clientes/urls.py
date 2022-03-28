from django.urls import path
from clientes import views

urlpatterns = [
    path('adicionar_cliente/', views.adicionar_cliente, name='adicionar_cliente'),
    path('listar_cliente/', views.listar_cliente, name='listar_cliente'),
]