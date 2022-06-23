from django.db import models

# Create your models here.
class Renovacao(models.Model):
    dataDesocupacao = models.DateField()
    dataRenovacao = models.DateField()
    cartorio = models.CharField(max_length=100)
    
