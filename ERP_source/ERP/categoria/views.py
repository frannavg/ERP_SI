from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Categoria
from  .forms import PostCategoria

def post_list(request):
    if request.user.is_authenticated:
        return render(request, "categoria/categoria.html")
    else:
        return HttpResponseRedirect('../login/')

def lista_categoria(request):
    if request.user.is_authenticated:
        categoria = Categoria.objects.all()
        contexto = {
            'categoria': categoria
            }
        return render(request, "categoria/listar_categoria.html", contexto)
    else:
        return HttpResponseRedirect('../../login/')

def insere_categoria(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostCategoria(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('../lista-categoria/')
        else:
            form = PostCategoria()
            return render(request, "categoria/inserir.html",{'form': form})

    else:
        return HttpResponseRedirect('../../login')

# Create your views here.
