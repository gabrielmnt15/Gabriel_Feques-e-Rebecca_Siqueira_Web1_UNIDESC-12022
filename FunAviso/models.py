from django.db import models

# Create your models here.
class FunAviso(models.Model):
    mensagem = models.CharField(max_length=100)