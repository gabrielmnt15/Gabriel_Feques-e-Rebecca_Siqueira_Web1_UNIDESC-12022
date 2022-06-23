from xml.parsers.expat import model
from django.db import models

# Create your models here.
class PessoaFisica(models.Model):
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=7)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    dataNascimento = models.DateField()
