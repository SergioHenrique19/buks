from django.shortcuts import render
from .forms import Cadastro_Emprestimo

# Create your views here.

def register_lending(request):

    data = {}

    form = Cadastro_Emprestimo(request.POST or None)
    if form.is_valid():
        # request.session['validRegisterBook'] = "sim"
        form.save()
        return render(request, 'Emprestimo/register_lending.html', data)
    else:
        # request.session['validRegisterBook'] = "nao"
        data['form'] = form
        return render(request, 'Emprestimo/register_lending.html', data)
