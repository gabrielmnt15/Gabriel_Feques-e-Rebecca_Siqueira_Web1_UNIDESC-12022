from pyexpat import model
from django.db import models

# Create your models here.
class Imovel(models.Model):
    matricula_imo = models.IntegerField()
    rua_imo = models.CharField(max_length=100)
    cep_imo = models.CharField(max_length=100)
    bairro_imo = models.CharField(max_length=100)
    cidade_imo = models.CharField(max_length=100)
    uf_imo = models.CharField(max_length=100)
    tamanho_imo = models.CharField(max_length=100)
    comodos_imo = models.CharField(max_length=100)
    garagem_imo = models.CharField(max_length=100)
    valor_imo = models.IntegerField()
    tipo_imo = models.CharField(max_length=100)
    status_imo = models.CharField(max_length=100)

    def incluir_Anuncio():
        pass

    def consultar_Anuncio():
        pass

    def alterar_Anuncio():
        pass

    def remover_Anuncio():
        pass
