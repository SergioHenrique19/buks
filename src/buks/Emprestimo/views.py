from django.shortcuts import render
from .forms import Cadastro_Emprestimo
from Cliente.models import Cliente
from Livros.models import Livro
from .models import Emprestimo
import decimal

# Create your views here.

def register_lending(request):

    data = {}

    data['Clientes'] = Cliente.objects.all()
    data['Livros'] = Livro.objects.all()
    request.session['validRegisterLending'] = "nao"    

    if request.method == "POST":
        id_emprestimo = request.POST['id_emprestimo']
        data_devolucao = request.POST['data_devolucao']
        try:
            cliente = Cliente.objects.get(cpf=request.POST.get('cliente', False))
            livro = Livro.objects.get(isbn=request.POST.get('livro', False))
        except:
            cliente = None
            livro = None
        try:
            preco_unitario = decimal.Decimal(request.POST['preco_unitario'].replace(",", "."))
        except:
            preco_unitario = None
        quantidade = int(request.POST['quantidade'])
        try:
            valor = decimal.Decimal(request.POST['valor'].replace(",", "."))
        except:
            valor = None
        if request.POST.get('forma_pagamento', False) == "0":
            forma_pagamento = int(0)
        else:
            forma_pagamento = int(1)
        try:
            desconto = decimal.Decimal(request.POST['desconto'].replace(",", "."))
        except:
            desconto = None
        try:
            valor_total = decimal.Decimal(request.POST['valor_total'].replace(",", "."))
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

