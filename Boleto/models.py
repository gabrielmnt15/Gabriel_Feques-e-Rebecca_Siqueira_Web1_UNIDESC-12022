from django.db import models

# Create your models here.
class Boleto(models.Model):
    codCliente = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100)