from django.db import models
from categoria.models import Categoria


class Produto(models.Model):
    codigoProduto =  models.AutoField(primary_key=True)
    fkCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precoCompra = models.FloatField(null=True, blank=False)
    name = models.CharField(max_length=50, blank=False)
    precoVenda = models.FloatField(null=True, blank=False)
    qtde = models.IntegerField(null=True, blank=False)
    fornecedor = models.CharField(max_length=50, blank=False)
    dataCompra = models.DateField(null=True)

    def __str__(self):
        return self.name




# Create your models here.
