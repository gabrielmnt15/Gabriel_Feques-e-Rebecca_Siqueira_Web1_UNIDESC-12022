from django.db import models

# Create your models here.
class Gerente(models.Model):
    comissao = models.IntegerField()

def calcular_Salario():
    pass
