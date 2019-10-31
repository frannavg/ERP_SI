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
    if request.user.is_authenticated:
        return render(request, "produto/produto.html")
    else:
        return HttpResponseRedirect('../login/')


def lista_produto(request):
    if request.user.is_authenticated:
        produto = Produto.objects.all()
        contexto = {
            'produto': produto
            }
        return render(request, "produto/listar_produto.html", contexto)
    else:
        return HttpResponseRedirect('../../login')


def insere_produto(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostProduto(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista/')
        else:
            form = PostProduto()
            return render(request, "produto/inserir.html",{'form': form})
    else:
        return HttpResponseRedirect('../../login')

class ProdutoList(generics.ListCreateAPIView):

        queryset = Produto.objects.all()
        serializer_class = ProdutoSerializer

# Create your views here.
