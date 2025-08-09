from django.db import models

class CategoriaMovimentacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class MovimentacaoFinanceira(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    categoria = models.ForeignKey(CategoriaMovimentacao, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.valor} em {self.data}"