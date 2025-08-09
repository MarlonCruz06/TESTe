from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_membros, name='lista_membros'),
    path('cadastrar/', views.cadastrar_membro, name='cadastrar_membro'),
    path('editar/<int:id>/', views.editar_membro, name='editar_membro'),
    path('excluir/<int:id>/', views.excluir_membro, name='excluir_membro'),
]