from django.db import models

# Create your models here.
class Funcionario(models.Model):
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    dataNascimento = models.DateField()
    carteiraTrabalho = models.CharField(max_length=100)
    salario = models.IntegerField()
    pis = models.CharField(max_length=100)

def consultar_Imoveis():
    pass

def manter_Anuncio():
    pass

def manter_Cliente():
    pass

def manter_Funcionario():
    pass

def manter_Agendamento():
    pass

def gerar_Relatorio():
    pass

def calcular_Salario():
    pass