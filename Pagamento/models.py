from django.db import models

# Create your models here.
class Pagamento(models.Model):
    valor_pag = models.IntegerField()
    forma_pag = models.CharField(max_length=100)
    parcelas_pag = models.IntegerField()
    data_pag = models.DateField()
    banco_pag = models.CharField(max_length=100)
    agencia_pag = models.CharField(max_length=100)
    conta_pag = models.CharField(max_length=100)