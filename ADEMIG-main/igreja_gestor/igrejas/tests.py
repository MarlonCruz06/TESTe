from django.test import TestCase
from .models import Igreja

class IgrejaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Igreja.objects.create(nome="Igreja Teste", endereco="Rua Teste, 123", telefone="123456789", email="teste@igreja.com", pastor_responsavel="Pastor Teste")

    def test_nome_label(self):
        igreja = Igreja.objects.get(id=1)
        field_label = igreja._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')

    def test_endereco_label(self):
        igreja = Igreja.objects.get(id=1)
        field_label = igreja._meta.get_field('endereco').verbose_name
        self.assertEqual(field_label, 'endereco')

    def test_telefone_label(self):
        igreja = Igreja.objects.get(id=1)
        field_label = igreja._meta.get_field('telefone').verbose_name
        self.assertEqual(field_label, 'telefone')

    def test_email_label(self):
        igreja = Igreja.objects.get(id=1)
        field_label = igreja._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_pastor_responsavel_label(self):
        igreja = Igreja.objects.get(id=1)
        field_label = igreja._meta.get_field('pastor_responsavel').verbose_name
        self.assertEqual(field_label, 'pastor responsavel')

    def test_nome_max_length(self):
        igreja = Igreja.objects.get(id=1)
        max_length = igreja._meta.get_field('nome').max_length
        self.assertEqual(max_length, 255)

    def test_email_max_length(self):
        igreja = Igreja.objects.get(id=1)
        max_length = igreja._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_object_representation(self):
        igreja = Igreja.objects.get(id=1)
        expected_object_name = f'{igreja.nome}'
        self.assertEqual(expected_object_name, str(igreja))