from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MovimentacaoFinanceira
from .forms import MovimentacaoFinanceiraForm
from django.db.models import Sum
from django.utils import timezone

@login_required
def listar_movimentacoes(request):
    movimentacoes = MovimentacaoFinanceira.objects.all()
    total_entradas = MovimentacaoFinanceira.objects.filter(tipo='entrada').aggregate(Sum('valor'))['valor__sum'] or 0
    total_saidas = MovimentacaoFinanceira.objects.filter(tipo='saida').aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = total_entradas - total_saidas
    return render(request, 'financeiro/listar_movimentacoes.html', {
        'movimentacoes': movimentacoes,
        'saldo': saldo,
    })

@login_required
def cadastrar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoFinanceiraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_movimentacoes')
    else:
        form = MovimentacaoFinanceiraForm()
    return render(request, 'financeiro/cadastrar_movimentacao.html', {'form': form})

@login_required
def editar_movimentacao(request, pk):
    movimentacao = MovimentacaoFinanceira.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovimentacaoFinanceiraForm(request.POST, instance=movimentacao)
        if form.is_valid():
            form.save()
            return redirect('listar_movimentacoes')
    else:
        form = MovimentacaoFinanceiraForm(instance=movimentacao)
    return render(request, 'financeiro/editar_movimentacao.html', {'form': form})

@login_required
def excluir_movimentacao(request, pk):
    movimentacao = MovimentacaoFinanceira.objects.get(pk=pk)
    if request.method == 'POST':
        movimentacao.delete()
        return redirect('listar_movimentacoes')
    return render(request, 'financeiro/excluir_movimentacao.html', {'movimentacao': movimentacao})