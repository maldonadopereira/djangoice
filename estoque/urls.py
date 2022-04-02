from django.urls import path
from estoque import views

urlpatterns = [
    path('entrada_estoque_list', views.entrada_estoque_list, name='entrada_estoque_list'),
    path('entrada_estoque_detail/<int:estoque_id>', views.entrada_estoque_detail, name='entrada_estoque_detail'),
    path('entrada_estoque_add/', views.entrada_estoque_add, name='entrada_estoque_add'),

    path('saida', views.saida_estoque, name='saida_estoque'),
]