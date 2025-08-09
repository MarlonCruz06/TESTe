from django.db import models
from membros.models import Membro
from eventos.models import Evento

class Inscricao(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.membro} inscrito em {self.evento}"