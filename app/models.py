from django.db import models

# Create your models here.

# classe criada a partir do exemplo de models no site do django


class Produtos(models.Model):  # colocado o nome da classe de produtos
    produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField(max_length=4)
    preco = models.FloatField(max_length=10)
