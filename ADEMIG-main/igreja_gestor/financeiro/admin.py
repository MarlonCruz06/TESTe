from django.contrib import admin
from .models import MovimentacaoFinanceira

class MovimentacaoFinanceiraAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'tipo')
    search_fields = ('descricao',)
    list_filter = ('tipo', 'data')

admin.site.register(MovimentacaoFinanceira, MovimentacaoFinanceiraAdmin)