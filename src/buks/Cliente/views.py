from django.shortcuts import render, redirect
from .forms import Cadastro_Cliente, Alterar_Cliente, Consultar_Cliente
from .models import Cliente
from datetime import datetime

# Create your views here.

def register_client(request):
    
    data = {}
    form = Cadastro_Cliente(request.POST or None)

    if form.is_valid():
        request.session['validRegisterClient'] = "sim"
        form.save()
        return render(request, 'Cliente/register_client.html', data)
    else:
        request.session['validRegisterClient'] = "nao"
        data['form'] = form
        return render(request, 'Cliente/register_client.html', data)


def update_client(request):

    data = {}

    try:
        if request.session['validUpdateClientCont'] == 0:
            request.session['validUpdateClient'] = "nao"
    except:
        None

    if request.method == "POST":
        name_client = request.POST['search_client']
        if name_client != "":
            clientes = Cliente.objects.filter(email=name_client)
            quant_clientes = Cliente.objects.filter(email=name_client).count()
            if quant_clientes == 0:
                return render(request, 'Cliente/update_client.html', data)
            else:
                data['Clientes'] = clientes
                return render(request, 'Cliente/update_client.html', data)

    data['Clientes'] = Cliente.objects.all()

    try:
        request.session['validUpdateClientCont'] = 0
    except:
        None

    return render(request, 'Cliente/update_client.html', data)

def update_client_form(request, pk):

    data = {}

    clientes = Cliente.objects.get(pk=pk)
    form = Alterar_Cliente(request.POST or None,
                         request.FILES or None, instance=clientes)

    if form.is_valid():
        request.session['validUpdateClient'] = 'sim'
        request.session['validUpdateClientCont'] = 1
        form.save()
        return redirect('Cliente:update_client')

    request.session['validUpdateClient'] = "nao"
    data['form'] = form

    return render(request, 'Cliente/update_client_form.html', data)

def read_client(request):
    
    data = {}

    if request.method == "POST":
        email_client = request.POST['search_client']
        if email_client != "":
            clientes = Cliente.objects.filter(email=email_client)
            quant_clientes = Cliente.objects.filter(email=email_client).count()
            if quant_clientes == 0:
                return render(request, 'Cliente/read_client.html', data)
            else:
                data['Clientes'] = clientes
                return render(request, 'Cliente/read_client.html', data)

    data['Clientes'] = Cliente.objects.all()

    return render(request, 'Cliente/read_client.html', data)

def read_client_form(request, pk):

    data = {}

    cliente = Cliente.objects.get(pk=pk)
    form = Consultar_Cliente(request.POST or None,
                           request.FILES or None, instance=cliente)

    data['Cliente'] = cliente
    data['form'] = form

    return render(request, 'Cliente/read_client_form.html', data)