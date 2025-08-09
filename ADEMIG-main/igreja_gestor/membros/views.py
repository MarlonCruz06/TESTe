from django.shortcuts import render, get_object_or_404, redirect
from .models import Membro
from .forms import MembroForm, MembroEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def listar_membros(request):
    membros = Membro.objects.all()
    return render(request, 'membros/listar_membros.html', {'membros': membros})

from django.contrib.auth import get_user_model

@login_required
def cadastrar_membro(request):
    if request.method == 'POST':
        form = MembroForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the user
            User = get_user_model()
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )

            # Create the member
            membro = form.save(commit=False)
            membro.user = user
            membro.igreja = form.cleaned_data['igreja']
            membro.save()

            messages.success(request, 'Membro cadastrado com sucesso!')
            return redirect('lista_membros')
    else:
        form = MembroForm()
    return render(request, 'membros/cadastrar_membro.html', {'form': form})

@login_required
def editar_membro(request, id):
    membro = get_object_or_404(Membro, id=id)
    if request.method == 'POST':
        form = MembroEditForm(request.POST, request.FILES, instance=membro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membro editado com sucesso!')
            return redirect('lista_membros')
    else:
        form = MembroEditForm(instance=membro)
    return render(request, 'membros/editar_membro.html', {'form': form, 'membro': membro})

@login_required
def excluir_membro(request, id):
    membro = get_object_or_404(Membro, id=id)
    if request.method == 'POST':
        membro.delete()
        messages.success(request, 'Membro excluído com sucesso!')
        return redirect('listar_membros')
    return render(request, 'membros/excluir_membro.html', {'membro': membro})