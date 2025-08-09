from django.contrib import admin
from .models import Membro

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'telefone', 'email', 'status', 'igreja')
    search_fields = ('nome', 'email', 'telefone')
    list_filter = ('status', 'igreja')
    ordering = ('nome',)