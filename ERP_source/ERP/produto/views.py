from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def post_list(request):
 return HttpResponse('Olá Mundo!')

def lista_produto(request):
    # Primeiro, buscamos os funcionarios
    produto = Produto.objects.all()

    # Incluímos no contexto
    contexto = {
      'produto': produto
    }

    # Retornamos o template no qual os funcionários serão dispostos
    #return render(request, "templates/produto.html", contexto)
    return HttpResponse('teste4')

# Create your views here.
