from django.db import models

class Igreja(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pastor_responsavel = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Igreja"
        verbose_name_plural = "Igrejas"