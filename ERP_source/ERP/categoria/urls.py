from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('list-companie/', views.lista_categoria, name='lista_categoria'),
    path('insere-categoria/', views.insere_categoria, name='insere_categoria'),
]
