from django import forms

from .models import Produto

class PostProduto(forms.ModelForm):
    dataCompra = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Produto
        fields = ('fkCategoria', 'precoCompra','name','precoVenda','qtde','fornecedor','dataCompra',)
