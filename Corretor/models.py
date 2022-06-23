from django.db import models

# Create your models here.
class Corretor(models.Model):
    comissao = models.IntegerField()
    idCorretor = models.CharField(max_length=100)

    def calcular_Salario():
        pass
