from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('membros/', include('membros.urls')),
    path('igrejas/', include('igrejas.urls')),
    path('eventos/', include('eventos.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('inscricoes/', include('inscricoes.urls')),
    path('dashboard/', include('dashboard.urls')),
]