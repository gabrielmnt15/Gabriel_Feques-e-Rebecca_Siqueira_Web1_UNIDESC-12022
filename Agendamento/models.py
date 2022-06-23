from pyexpat import model
from django.db import models

# Create your models here.
class Agendamento(models.Model):
    dia = models.DateField()
    hora = models.DateField()
    local = models.CharField(max_length=100)

    def incluir_Agendamento():
        pass

    def consultar_Agendamento():
        pass

    def alterar_Agendamento():
        pass

    def remover_Agendamento():
        pass
