from django.test import TestCase
from django.contrib.auth import get_user_model

class UsuarioModelTest(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.usuario = self.User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

    def test_usuario_criado(self):
        self.assertEqual(self.usuario.username, 'testuser')
        self.assertEqual(self.usuario.email, 'testuser@example.com')
        self.assertTrue(self.usuario.check_password('testpassword'))

    def test_usuario_str(self):
        self.assertEqual(str(self.usuario), 'testuser')

    def test_usuario_email(self):
        self.assertEqual(self.usuario.email, 'testuser@example.com')

    def test_usuario_permissoes(self):
        self.usuario.is_staff = True
        self.usuario.save()
        self.assertTrue(self.usuario.is_staff)