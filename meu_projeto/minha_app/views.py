from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def contatos(request):
    return render(request, 'contatos.html')

def sobre(request):
    return render(request, 'sobre.html')

def endereco(request):
    return render (request, 'endereco.html')

def cadastro_cliente(request):
    if request.method == 'post':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        Cliente.objects.crete(nome=nome, telefone=telefone, email=email)


    return render(request, 'cadastro_cliente.html')

def cadastro_produto(request):
    if request.method == 'post':
        nome = request.POST['nome']
        quantidade = request.POST['quantidade']
        descricao = request.POST['descrição']
        Produto.objects.create(nome=nome, quantidade=quantidade, descricao=descricao)

    return render(request, 'cadastro_produto.html')