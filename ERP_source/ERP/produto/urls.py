from django.urls import path
from django.contrib import admin
from .views import ProdutoList
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('lista/', views.lista_produto, name='lista_produto'),
    path('insere/', views.insere_produto, name='insere_produto'),
    path('listaWeb/', views.ProdutoList.as_view(), name='ProdutoList'),

]
