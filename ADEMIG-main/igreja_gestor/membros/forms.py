from django import forms
from .models import Membro
from igrejas.models import Igreja
from django.contrib.auth import get_user_model

class MembroForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    igreja = forms.ModelChoiceField(queryset=Igreja.objects.all())

    class Meta:
        model = Membro
        fields = ['nome', 'data_nascimento', 'telefone', 'email', 'endereco', 'foto_perfil', 'status']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'foto_perfil': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'nome': 'Nome',
            'data_nascimento': 'Data de Nascimento',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'endereco': 'Endereço',
            'foto_perfil': 'Foto de Perfil',
            'status': 'Status',
        }
        help_texts = {
            'nome': 'Insira o nome completo do membro.',
            'telefone': 'Insira um número de telefone válido.',
            'email': 'Insira um endereço de e-mail válido.',
            'endereco': 'Insira o endereço completo do membro.',
        }

class MembroEditForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'data_nascimento', 'telefone', 'email', 'endereco', 'foto_perfil', 'status', 'igreja']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'foto_perfil': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'nome': 'Nome',
            'data_nascimento': 'Data de Nascimento',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'endereco': 'Endereço',
            'foto_perfil': 'Foto de Perfil',
            'status': 'Status',
            'igreja': 'Igreja',
        }