from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('<slug:token>', views.autentica_token, name='autentica_token'),

]
