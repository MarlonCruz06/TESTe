from django.urls import path
from .views import (
    ListarEventosView,
    DetalharEventoView,
    CriarEventoView,
    EditarEventoView,
    ExcluirEventoView,
)

app_name = 'eventos'

urlpatterns = [
    path('', ListarEventosView.as_view(), name='listar_eventos'),
    path('novo/', CriarEventoView.as_view(), name='criar_evento'),
    path('editar/<int:pk>/', EditarEventoView.as_view(), name='editar_evento'),
    path('excluir/<int:pk>/', ExcluirEventoView.as_view(), name='excluir_evento'),
    path('<int:pk>/', DetalharEventoView.as_view(), name='detalhar_evento'),
]
