from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Categoria
from  .forms import PostCategoria

def post_list(request):
 return render(request, "categoria/categoria.html")

def lista_categoria(request):
    # Primeiro, buscamos os funcionarios
    categoria = Categoria.objects.all()

    # Incluímos no contexto
    contexto = {
      'categoria': categoria
    }

    # Retornamos o template no qual os funcionários serão dispostos
    return render(request, "categoria/listar_categoria.html", contexto)
    #return HttpResponse('teste4')

def insere_categoria(request):
    if request.method == "POST":
        form = PostCategoria(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('../lista-categoria/')
    else:
         form = PostCategoria()
    return render(request, "categoria/inserir.html",{'form': form})


# Create your views here.
