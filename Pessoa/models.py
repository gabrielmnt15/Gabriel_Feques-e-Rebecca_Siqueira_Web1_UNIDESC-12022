from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Pessoa(models.Model):
    matricula = models.IntegerField()
    telefone = models.CharField(max_length=11)
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=50)
