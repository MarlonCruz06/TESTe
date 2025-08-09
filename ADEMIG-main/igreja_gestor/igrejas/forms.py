from django import forms
from .models import Igreja

class IgrejaForm(forms.ModelForm):
    class Meta:
        model = Igreja
        fields = ['nome', 'endereco', 'telefone', 'email', 'pastor_responsavel']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pastor_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome da Igreja',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'pastor_responsavel': 'Pastor Responsável',
        }
        help_texts = {
            'nome': 'Insira o nome completo da igreja.',
            'endereco': 'Insira o endereço completo.',
            'telefone': 'Insira um número de telefone válido.',
            'email': 'Insira um e-mail válido.',
            'pastor_responsavel': 'Insira o nome do pastor responsável.',
        }