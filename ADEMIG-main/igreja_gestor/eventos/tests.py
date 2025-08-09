from django.test import TestCase
from .models import Evento
from django.utils import timezone

class EventoModelTest(TestCase):

    def setUp(self):
        self.evento = Evento.objects.create(
            titulo="Culto de Louvor",
            data=timezone.now(),
            descricao="Um culto especial de louvor e adoração.",
            local="Igreja Central",
            imagem="caminho/para/imagem.jpg"
        )

    def test_evento_criado(self):
        self.assertEqual(self.evento.titulo, "Culto de Louvor")
        self.assertEqual(self.evento.local, "Igreja Central")

    def test_evento_str(self):
        self.assertEqual(str(self.evento), "Culto de Louvor")