from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'local', 'descricao')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data',)

admin.site.register(Evento, EventoAdmin)