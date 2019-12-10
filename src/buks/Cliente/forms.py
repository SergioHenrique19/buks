from django.forms import ModelForm
from django import forms
from .models import Cliente

# Classe de formatação de input do tipo date(data).
class DateInput(forms.DateInput):
    input_type = 'date'

# Formulário utiliado para cadastrar um cliente no sistema.
class Cadastro_Cliente(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'data_nasc': DateInput(format='%Y-%m-%d')
        }

# Formulário utilizado para atualizar os dados de um cliente no sistema.
class Alterar_Cliente(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'data_nasc': DateInput(format='%Y-%m-%d')
        }

# Formulário utilizado para consultar os dados de um cliente do sistema.
class Consultar_Cliente(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'data_nasc': DateInput(format='%Y-%m-%d')
        }
