from django import forms

from .models import Categoria

class PostCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('codigoCategoria','name',)
