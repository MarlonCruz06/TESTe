from django.contrib import admin
from .models import Inscricao

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'membro', 'data_inscricao', 'pago')
    search_fields = ('evento__titulo', 'membro__nome')
    list_filter = ('pago',)
    ordering = ('-data_inscricao',)