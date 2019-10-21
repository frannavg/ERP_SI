from django import forms

from .models import Produto

class PostProduto(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('fkCategoria', 'precoCompra','name','precoVenda','qtde','fornecedor',)
