from django.db import models

# Create your models here.
class Contrato(models.Model):
    dadosCliente = models.CharField(max_length=100)
    dadosCorretor = models.CharField(max_length=100)
    descricaoImovel = models.CharField(max_length=100)
    valor = models.IntegerField()
    documentacao = models.CharField(max_length=100)
    clausulaPenal = models.CharField(max_length=100)