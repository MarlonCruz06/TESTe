from django.test import TestCase
from .models import Inscricao
from membros.models import Membro
from eventos.models import Evento
from igrejas.models import Igreja
from django.contrib.auth import get_user_model
from django.utils import timezone

class InscricaoModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.igreja = Igreja.objects.create(
            nome="Igreja Teste",
            endereco="Rua Teste, 123",
            pastor_responsavel="Pastor Teste"
        )
        self.membro = Membro.objects.create(
            user=self.user,
            igreja=self.igreja,
            nome="João da Silva",
            data_nascimento="1990-01-01",
            telefone="123456789",
            email="joao@example.com",
            endereco="Rua A, 123"
        )
        self.evento = Evento.objects.create(
            titulo="Culto de Adoração",
            data=timezone.now(),
            descricao="Um culto especial de adoração.",
            local="Igreja Central"
        )
        self.inscricao = Inscricao.objects.create(
            membro=self.membro,
            evento=self.evento
        )

    def test_inscricao_creation(self):
        self.assertEqual(self.inscricao.membro.nome, "João da Silva")
        self.assertEqual(self.inscricao.evento.titulo, "Culto de Adoração")

    def test_str_method(self):
        self.assertEqual(str(self.inscricao), f"{self.membro} inscrito em {self.evento}")

    def test_inscricao_evento(self):
        self.assertEqual(self.inscricao.evento, self.evento)

    def test_inscricao_membro(self):
        self.assertEqual(self.inscricao.membro, self.membro)