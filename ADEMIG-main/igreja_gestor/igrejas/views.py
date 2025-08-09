from django.shortcuts import render, get_object_or_404, redirect
from .models import Igreja
from .forms import IgrejaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class IgrejaListView(LoginRequiredMixin, View):
    def get(self, request):
        igrejas = Igreja.objects.all()
        return render(request, 'igrejas/lista.html', {'igrejas': igrejas})

class IgrejaCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = IgrejaForm()
        return render(request, 'igrejas/form.html', {'form': form})

    def post(self, request):
        form = IgrejaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('igrejas:lista')
        return render(request, 'igrejas/form.html', {'form': form})

class IgrejaUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        igreja = get_object_or_404(Igreja, pk=pk)
        form = IgrejaForm(instance=igreja)
        return render(request, 'igrejas/form.html', {'form': form})

    def post(self, request, pk):
        igreja = get_object_or_404(Igreja, pk=pk)
        form = IgrejaForm(request.POST, instance=igreja)
        if form.is_valid():
            form.save()
            return redirect('igrejas:lista')
        return render(request, 'igrejas/form.html', {'form': form})

class IgrejaDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        igreja = get_object_or_404(Igreja, pk=pk)
        return render(request, 'igrejas/excluir_igreja.html', {'igreja': igreja})

    def post(self, request, pk):
        igreja = get_object_or_404(Igreja, pk=pk)
        igreja.delete()
        return redirect('igrejas:lista')