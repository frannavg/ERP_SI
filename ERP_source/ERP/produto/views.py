from django.shortcuts import render
from django import forms
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Produto
from  .forms import PostProduto
from .serializers import ProdutoSerializer
from rest_framework import generics



def post_list(request):
 return render(request, "produto/produto.html")

def lista_produto(request):
    # Primeiro, buscamos os funcionarios
    produto = Produto.objects.all()

    # Incluímos no contexto
    contexto = {
      'produto': produto
    }

    # Retornamos o template no qual os funcionários serão dispostos
    return render(request, "produto/listar_produto.html", contexto)
    #return HttpResponse('teste4')

def insere_produto(request):
    if request.method == "POST":
        form = PostProduto(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('../lista/')
    else:
         form = PostProduto()
    return render(request, "produto/inserir.html",{'form': form})

class ProdutoList(generics.ListCreateAPIView):

        queryset = Produto.objects.all()
        serializer_class = ProdutoSerializer
        
# Create your views here.
