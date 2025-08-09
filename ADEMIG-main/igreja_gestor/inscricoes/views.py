from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Inscricao
from .forms import InscricaoForm
from membros.models import Membro

@login_required
def listar_inscricoes(request):
    try:
        membro = request.user.membro
        inscricoes = Inscricao.objects.filter(membro=membro)
    except Membro.DoesNotExist:
        inscricoes = []
    return render(request, 'inscricoes/listar_inscricoes.html', {'inscricoes': inscricoes})

@login_required
def criar_inscricao(request):
    try:
        membro = request.user.membro
    except Membro.DoesNotExist:
        # Handle the case where the user is not a member
        # You might want to redirect them to a page to create a member profile
        return redirect('dashboard')

    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.membro = membro
            inscricao.save()
            return redirect('listar_inscricoes')
    else:
        form = InscricaoForm()
    return render(request, 'inscricoes/criar_inscricao.html', {'form': form})

@login_required
def editar_inscricao(request, id):
    inscricao = Inscricao.objects.get(id=id)
    if request.method == 'POST':
        form = InscricaoForm(request.POST, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('listar_inscricoes')
    else:
        form = InscricaoForm(instance=inscricao)
    return render(request, 'inscricoes/editar_inscricao.html', {'form': form})

@login_required
def excluir_inscricao(request, id):
    inscricao = Inscricao.objects.get(id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('listar_inscricoes')
    return render(request, 'inscricoes/excluir_inscricao.html', {'inscricao': inscricao})