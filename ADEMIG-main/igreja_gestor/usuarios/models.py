from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Níveis de acesso
    ADMINISTRADOR = 'admin'
    LIDERANCA = 'lider'
    MEMBRO = 'membro'

    NIVEL_ACESSO_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (LIDERANCA, 'Pastor/Liderança'),
        (MEMBRO, 'Membro'),
    ]

    nivel_acesso = models.CharField(
        max_length=10,
        choices=NIVEL_ACESSO_CHOICES,
        default=MEMBRO,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'