from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff')

admin.site.register(Usuario, UsuarioAdmin)

# Personalização do painel administrativo
admin.site.site_header = "Painel de Controle da Igreja"
admin.site.site_title = "Administração da Igreja"
admin.site.index_title = "Bem-vindo ao Painel de Administração"