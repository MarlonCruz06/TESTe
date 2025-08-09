from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class ListarEventosView(LoginRequiredMixin, View):
    def get(self, request):
        eventos = Evento.objects.all()
        return render(request, 'eventos/evento_list.html', {'eventos': eventos})

class DetalharEventoView(LoginRequiredMixin, View):
    def get(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        return render(request, 'eventos/evento_detail.html', {'evento': evento})

class CriarEventoView(LoginRequiredMixin, View):
    def get(self, request):
        form = EventoForm()
        return render(request, 'eventos/evento_form.html', {'form': form})

    def post(self, request):
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save()
            return redirect('eventos:detalhar_evento', pk=evento.pk)
        return render(request, 'eventos/evento_form.html', {'form': form})

class EditarEventoView(LoginRequiredMixin, View):
    def get(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        form = EventoForm(instance=evento)
        return render(request, 'eventos/evento_form.html', {'form': form})

    def post(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('eventos:detalhar_evento', pk=evento.pk)
        return render(request, 'eventos/evento_form.html', {'form': form})

class ExcluirEventoView(LoginRequiredMixin, View):
    def get(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        return render(request, 'eventos/evento_confirm_delete.html', {'evento': evento})

    def post(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        evento.delete()
        return redirect('eventos:listar_eventos')
