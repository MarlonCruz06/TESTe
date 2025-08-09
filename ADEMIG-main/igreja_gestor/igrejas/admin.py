from django.contrib import admin
from .models import Igreja

@admin.register(Igreja)
class IgrejaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'email', 'pastor_responsavel')
    search_fields = ('nome', 'pastor_responsavel')
    list_filter = ('pastor_responsavel',)