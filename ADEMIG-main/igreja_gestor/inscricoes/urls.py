from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_inscricoes, name='lista_inscricoes'),
    path('nova/', views.criar_inscricao, name='nova_inscricao'),
    path('<int:pk>/editar/', views.editar_inscricao, name='editar_inscricao'),
    path('<int:pk>/excluir/', views.excluir_inscricao, name='excluir_inscricao'),
]