from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from eventos.models import Evento
from financeiro.models import MovimentacaoFinanceira
from membros.models import Membro
from django.utils import timezone
from django.db.models import Sum

@login_required
def dashboard(request):
    # Obtendo eventos próximos
    eventos_proximos = Evento.objects.filter(data__gte=timezone.now()).order_by('data')[:5]

    # Obtendo movimentações financeiras do mês atual
    movimentacoes = MovimentacaoFinanceira.objects.filter(data__month=timezone.now().month, data__year=timezone.now().year)

    # Contando aniversariantes do mês
    aniversariantes = Membro.objects.filter(data_nascimento__month=timezone.now().month)

    # Resumo financeiro
    total_entradas = movimentacoes.filter(tipo='entrada').aggregate(total=Sum('valor'))['total'] or 0
    total_saidas = movimentacoes.filter(tipo='saida').aggregate(total=Sum('valor'))['total'] or 0

    context = {
        'eventos_proximos': eventos_proximos,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'aniversariantes': aniversariantes,
    }

    return render(request, 'dashboard/dashboard.html', context)