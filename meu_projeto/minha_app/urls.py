
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contatos/', views.contatos, name='contatos'),
    path('sobre/', views.sobre, name='sobre'),
    path('endereço/', views.endereco, name='endereço'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
]
