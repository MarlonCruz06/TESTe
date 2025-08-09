from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Membro
from igrejas.models import Igreja

class MembroModelTest(TestCase):

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
            endereco="Rua A, 123",
            status="ativo"
        )

    def test_membro_criado(self):
        membro = Membro.objects.get(nome="João da Silva")
        self.assertEqual(membro.telefone, "123456789")
        self.assertEqual(membro.status, "ativo")
        self.assertEqual(membro.user.username, "testuser")
        self.assertEqual(membro.igreja.nome, "Igreja Teste")

class MembroViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.igreja = Igreja.objects.create(
            nome="Igreja Teste",
            endereco="Rua Teste, 123",
            pastor_responsavel="Pastor Teste"
        )

    def test_cadastrar_membro_view(self):
        response = self.client.get(reverse('cadastrar_membro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'membros/cadastrar_membro.html')

        response = self.client.post(reverse('cadastrar_membro'), {
            'username': 'newuser',
            'password': 'newpassword',
            'igreja': self.igreja.id,
            'nome': 'Maria Oliveira',
            'data_nascimento': '1985-05-05',
            'telefone': '987654321',
            'email': 'maria@example.com',
            'endereco': 'Rua B, 456',
            'status': 'ativo'
        })
        self.assertEqual(response.status_code, 302) # Should redirect after successful creation
        self.assertTrue(Membro.objects.filter(nome="Maria Oliveira").exists())
        self.assertTrue(get_user_model().objects.filter(username="newuser").exists())