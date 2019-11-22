from django.shortcuts import render, redirect
from .forms import Cadastro_Livro
from django.contrib.auth.decorators import login_required
import decimal
from .models import Livro
import time

# Create your views here.

# Função que realiza o cadastro de um livro no sistema.
@login_required
def register_book(request):

    data = {}

    form = Cadastro_Livro(request.POST or None, request.FILES or None)
    if form.is_valid():
        request.session['validRegisterBook'] = "sim"
        form.save()
        return render(request, 'Livros/register_book.html', data)
    else:
        request.session['validRegisterBook'] = "nao"
        data['form'] = form
        return render(request, 'Livros/register_book.html', data)
