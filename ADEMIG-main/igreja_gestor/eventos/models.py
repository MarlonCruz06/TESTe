from django.db import models
from django.utils import timezone

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    local = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    quantidade_vagas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo
