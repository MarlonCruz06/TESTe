from django import forms
from .models import MovimentacaoFinanceira

class MovimentacaoFinanceiraForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoFinanceira
        fields = ['tipo', 'categoria', 'valor', 'data', 'descricao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'tipo': 'Tipo',
            'categoria': 'Categoria',
            'valor': 'Valor',
            'data': 'Data',
            'descricao': 'Descrição',
        }