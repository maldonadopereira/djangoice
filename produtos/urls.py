from django.urls import path
from produtos import views

urlpatterns = [
    path('add_produto', views.add_produto, name='add_produto'),
    path('edit_produto', views.edit_produto, name='edit_produto'),
]