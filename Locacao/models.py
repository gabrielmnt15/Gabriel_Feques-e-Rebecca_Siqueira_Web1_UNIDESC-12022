from pyexpat import model
from django.db import models

# Create your models here.
class Locacao(models.Model):
    dataDesocupacao = models.DateField()
    periodo = models.DateField()
    formaGarantia = models.CharField(max_length=100)
    fiador = models.CharField(max_length=100)
