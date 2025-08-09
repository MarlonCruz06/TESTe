from django.urls import path
from .views import (
    IgrejaListView,
    IgrejaCreateView,
    IgrejaUpdateView,
    IgrejaDeleteView,
)

app_name = 'igrejas'

urlpatterns = [
    path('', IgrejaListView.as_view(), name='lista'),
    path('novo/', IgrejaCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', IgrejaUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>/', IgrejaDeleteView.as_view(), name='excluir'),
]
