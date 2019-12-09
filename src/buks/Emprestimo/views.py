from django.shortcuts import render, redirect
from .forms import Alterar_Emprestimo, Consultar_Emprestimo
from Cliente.models import Cliente
from Livros.models import Livro
from .models import Emprestimo
import decimal
from django.contrib.auth.decorators import login_required
from datetime import datetime as dt

# Create your views here.


@login_required
def register_lending(request):

    data = {}

    data['Clientes'] = Cliente.objects.all()
    data['Livros'] = Livro.objects.all()
    request.session['validRegisterLending'] = "nao"

    if request.method == "POST":
        id_emprestimo = request.POST['id_emprestimo']
        data_devolucao = request.POST['data_devolucao']
        try:
            cliente = Cliente.objects.get(
                cpf=request.POST.get('cliente', False))
            livro = Livro.objects.get(isbn=request.POST.get('livro', False))
        except:
            cliente = None
            livro = None
        try:
            preco_unitario = decimal.Decimal(
                request.POST['preco_unitario'].replace(",", "."))
        except:
            preco_unitario = None
        quantidade = request.POST['quantidade']
        try:
            valor = decimal.Decimal(request.POST['valor'].replace(",", "."))
        except:
            valor = None
        if request.POST.get('forma_pagamento', False) == "0":
            forma_pagamento = int(0)
        else:
            forma_pagamento = int(1)
        try:
            desconto = decimal.Decimal(
                request.POST['desconto'].replace(",", "."))
        except:
            desconto = None
        try:
            valor_total = decimal.Decimal(
                request.POST['valor_total'].replace(",", "."))
        except:
            valor_total = None
        try:
            if int(livro.quantidade) >= int(quantidade) and int(quantidade) != 0:
                emprestimo = Emprestimo.objects.create(id_emprestimo=id_emprestimo, data_devolucao=data_devolucao, cliente=cliente,
                                                       livro=livro, preco_unitario=preco_unitario, quantidade=quantidade,
                                                       valor=valor, forma_pagamento=forma_pagamento, desconto=desconto,
                                                       valor_total=valor_total)
                emprestimo.save()
                livro.quantidade -= quantidade
                livro.save()
                request.session['validRegisterLending'] = "sim"

            return render(request, 'Emprestimo/register_lending.html', data)
        except:
            data['id_emprestimo'] = id_emprestimo
            data['data_devolucao'] = data_devolucao
            data['cliente'] = cliente
            data['livro'] = livro
            data['preco_unitario'] = preco_unitario
            data['quantidade'] = quantidade
            data['valor'] = valor
            data['forma_pagamento'] = forma_pagamento
            data['desconto'] = desconto
            data['valor_total'] = valor_total

            return render(request, 'Emprestimo/register_lending.html', data)
    else:
        data['id_emprestimo'] = None
        data['data_devolucao'] = None
        data['cliente'] = None
        data['livro'] = None
        data['preco_unitario'] = None
        data['quantidade'] = None
        data['valor'] = None
        data['forma_pagamento'] = None
        data['desconto'] = None
        data['valor_total'] = None

        return render(request, 'Emprestimo/register_lending.html', data)


@login_required
def update_lending(request):

    data = {}

    try:
        if request.session['validUpdateLendingCont'] == 0:
            request.session['validUpdateLending'] = "nao"
    except:
        None

    if request.method == "POST":
        id_emprestimo = request.POST['search_lending']
        if id_emprestimo != "":
            emprestimo = Emprestimo.objects.filter(id_emprestimo=id_emprestimo)
            quant_emprestimos = Emprestimo.objects.filter(
                id_emprestimo=id_emprestimo).count()
            if quant_emprestimos == 0:
                return render(request, 'Emprestimo/update_lending.html', data)
            else:
                data['Emprestimos'] = emprestimo
                return render(request, 'Emprestimo/update_lending.html', data)

    data['Emprestimos'] = Emprestimo.objects.all()

    try:
        request.session['validUpdateLendingCont'] = 0
    except:
        None

    return render(request, 'Emprestimo/update_lending.html', data)


@login_required
def update_lending_form(request, pk):

    data = {}

    emprestimo = Emprestimo.objects.get(pk=pk)
    data['form'] = Alterar_Emprestimo(instance=emprestimo)

    if request.method == "POST":
        id_emprestimo = request.POST['id_emprestimo']
        data_devolucao = request.POST['data_devolucao']
        try:
            cliente = Cliente.objects.get(
                cpf=request.POST.get('cliente', False))
            livro = Livro.objects.get(isbn=request.POST.get('livro', False))
        except:
            cliente = emprestimo.livro
            livro = emprestimo.cliente
        try:
            preco_unitario = decimal.Decimal(
                request.POST['preco_unitario'].replace(",", "."))
        except:
            preco_unitario = emprestimo.preco_unitario
        quantidade = int(request.POST['quantidade'])
        try:
            valor = decimal.Decimal(request.POST['valor'].replace(",", "."))
        except:
            valor = emprestimo.valor
        if request.POST.get('forma_pagamento', False) == "0":
            forma_pagamento = int(0)
        else:
            forma_pagamento = int(1)
        try:
            desconto = decimal.Decimal(
                request.POST['desconto'].replace(",", "."))
        except:
            desconto = emprestimo.valor
        try:
            valor_total = decimal.Decimal(
                request.POST['valor_total'].replace(",", "."))
        except:
            valor_total = emprestimo.valor_total

        if int(emprestimo.quantidade) <= int(quantidade) and int(emprestimo.livro.quantidade) >= int(quantidade) - int(emprestimo.quantidade):
            maior = int(emprestimo.quantidade) - int(quantidade)
            menor = 0
            maior_verifica = True
            menor_verifica = False
        else:
            if int(emprestimo.quantidade) > int(quantidade):
                menor = int(quantidade) - int(emprestimo.quantidade)
                maior = emprestimo.livro.quantidade + 1
                maior_verifica = False
                menor_verifica = True
        try:
            if(int(emprestimo.livro.quantidade) >= int(maior) and maior_verifica):
                print('entrou if 1')
                emprestimo.id_emprestimo = id_emprestimo
                emprestimo.data_devolucao = data_devolucao
                emprestimo.livro = livro
                emprestimo.cliente = cliente
                emprestimo.preco_unitario = preco_unitario
                emprestimo.quantidade = quantidade
                emprestimo.valor = valor
                emprestimo.forma_pagamento = forma_pagamento
                emprestimo.desconto = desconto
                emprestimo.valor_total = valor_total
                emprestimo.save()
                print('salvou emprestimo')
                request.session['validUpdateLending'] = 'sim'
                request.session['validUpdateLendingCont'] = 1
                livro.quantidade += int(maior)
                livro.save()
                print("salvou livro")

                return redirect('Emprestimo:update_lending')
            elif menor_verifica:
                print('entrou if 2')
                emprestimo.id_emprestimo = id_emprestimo
                emprestimo.data_devolucao = data_devolucao
                emprestimo.livro = livro
                emprestimo.cliente = cliente
                emprestimo.preco_unitario = preco_unitario
                emprestimo.quantidade = quantidade
                emprestimo.valor = valor
                emprestimo.forma_pagamento = forma_pagamento
                emprestimo.desconto = desconto
                emprestimo.valor_total = valor_total
                emprestimo.save()
                print('salvou emprestimo')
                request.session['validUpdateLending'] = 'sim'
                request.session['validUpdateLendingCont'] = 1
                livro.quantidade -= int(menor)
                livro.save()
                print('salvou livro')

                return redirect('Emprestimo:update_lending')

        except:
            data['id_emprestimo'] = id_emprestimo
            data['cliente'] = cliente
            data['livro'] = livro
            data['preco_unitario'] = preco_unitario
            data['quantidade'] = quantidade
            data['valor'] = valor
            data['forma_pagamento'] = forma_pagamento
            if data['forma_pagamento'] == 0:
                data['nome_pagamento'] = "Dinheiro"
            else:
                data['nome_pagamento'] = "Cartão de Crédito"
            data['desconto'] = desconto
            data['valor_total'] = valor_total
            request.session['validUpdateLending'] = "nao"

            return render(request, 'Emprestimo/update_lending_form.html', data)
    else:
        data['id_emprestimo'] = emprestimo.id_emprestimo
        data['cliente'] = emprestimo.cliente
        data['livro'] = emprestimo.livro
        data['preco_unitario'] = emprestimo.preco_unitario
        data['quantidade'] = emprestimo.quantidade
        data['valor'] = emprestimo.valor
        data['forma_pagamento'] = emprestimo.forma_pagamento
        if data['forma_pagamento'] == 0:
            data['nome_pagamento'] = "Dinheiro"
        else:
            data['nome_pagamento'] = "Cartão de Crédito"
        data['desconto'] = emprestimo.desconto
        data['valor_total'] = emprestimo.valor_total

    request.session['validUpdateLending'] = "nao"

    return render(request, 'Emprestimo/update_lending_form.html', data)


@login_required
def read_lending(request):

    data = {}

    if request.method == "POST":
        id_emprestimo = request.POST['search_lending']
        if id_emprestimo != "":
            emprestimo = Emprestimo.objects.filter(id_emprestimo=id_emprestimo)
            quant_emprestimos = Emprestimo.objects.filter(
                id_emprestimo=id_emprestimo).count()
            if quant_emprestimos == 0:
                return render(request, 'Emprestimo/read_lending.html', data)
            else:
                data['Emprestimos'] = emprestimo
                return render(request, 'Emprestimo/read_lending.html', data)

    data['Emprestimos'] = Emprestimo.objects.all()

    return render(request, 'Emprestimo/read_lending.html', data)


@login_required
def read_lending_form(request, pk):

    data = {}

    emprestimo = Emprestimo.objects.get(pk=pk)
    data['form'] = Consultar_Emprestimo(instance=emprestimo)

    data['id_emprestimo'] = emprestimo.id_emprestimo
    data['cliente'] = emprestimo.cliente
    data['livro'] = emprestimo.livro
    data['preco_unitario'] = emprestimo.preco_unitario
    data['quantidade'] = emprestimo.quantidade
    data['valor'] = emprestimo.valor
    data['forma_pagamento'] = emprestimo.forma_pagamento
    if data['forma_pagamento'] == 0:
        data['nome_pagamento'] = "Dinheiro"
    else:
        data['nome_pagamento'] = "Cartão de Crédito"
    data['desconto'] = emprestimo.desconto
    data['valor_total'] = emprestimo.valor_total

    return render(request, 'Emprestimo/read_lending_form.html', data)
