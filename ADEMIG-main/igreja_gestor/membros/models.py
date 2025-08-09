from django.db import models
from django.conf import settings

class Membro(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('visitante', 'Visitante'),
        ('afastado', 'Afastado'),
    ]

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField()
    igreja = models.ForeignKey('igrejas.Igreja', on_delete=models.CASCADE, related_name='membros')
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'