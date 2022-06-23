from django.db import models

# Create your models here.
class PessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=15)
    razaoSocial = models.CharField(max_length=100)
    representanteLegal = models.CharField(max_length=100)