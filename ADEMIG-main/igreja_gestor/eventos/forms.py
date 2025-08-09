from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'data', 'descricao', 'local', 'imagem']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'titulo': 'Título',
            'data': 'Data',
            'descricao': 'Descrição',
            'local': 'Local',
            'imagem': 'Imagem (opcional)',
        }