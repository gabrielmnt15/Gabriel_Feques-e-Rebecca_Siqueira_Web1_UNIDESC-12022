from pyexpat import model
from django.db import models

# Create your models here.
class Aviso(models.Model):
    matricula_avi = models.IntegerField()
    assunto_avi = models.CharField(max_length=100)
    data_avi = models.DateField()

    def incluir_Aviso():
        pass

    def consultar_Aviso():
        pass

    def remover_Aviso():
        pass