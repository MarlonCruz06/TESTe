from django.test import TestCase
from .models import MovimentacaoFinanceira, CategoriaMovimentacao
from django.db.models import Sum
from django.utils import timezone

class MovimentacaoFinanceiraTestCase(TestCase):
    def setUp(self):
        self.categoria = CategoriaMovimentacao.objects.create(nome='Teste')
        MovimentacaoFinanceira.objects.create(
            tipo='entrada',
            categoria=self.categoria,
            data=timezone.now(),
            descricao='Oferta',
            valor=100.00
        )
        MovimentacaoFinanceira.objects.create(
            tipo='saida',
            categoria=self.categoria,
            data=timezone.now(),
            descricao='Despesa com aluguel',
            valor=500.00
        )

    def test_movimentacao_financeira_entrada(self):
        entrada = MovimentacaoFinanceira.objects.get(descricao='Oferta')
        self.assertEqual(entrada.tipo, 'entrada')
        self.assertEqual(entrada.valor, 100.00)

    def test_movimentacao_financeira_saida(self):
        saida = MovimentacaoFinanceira.objects.get(descricao='Despesa com aluguel')
        self.assertEqual(saida.tipo, 'saida')
        self.assertEqual(saida.valor, 500.00)

    def test_movimentacao_financeira_total(self):
        total_entradas = MovimentacaoFinanceira.objects.filter(tipo='entrada').aggregate(Sum('valor'))['valor__sum']
        total_saidas = MovimentacaoFinanceira.objects.filter(tipo='saida').aggregate(Sum('valor'))['valor__sum']
        self.assertEqual(total_entradas, 100.00)
        self.assertEqual(total_saidas, 500.00)