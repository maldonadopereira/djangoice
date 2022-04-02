from django.contrib import admin
from .models import Estoque, EstoqueItens


class EstoqueItensInLine(admin.TabularInline):
    model = EstoqueItens
    extra = 0

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = EstoqueItensInLine,
    list_display = ('id', 'movimento')
    search_fields = ('id',)
    list_per_page = 20
    date_hierarchy = 'created'
    list_filter = ('funcionario',)



