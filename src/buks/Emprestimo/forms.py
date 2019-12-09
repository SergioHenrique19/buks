from django.forms import ModelForm
from .models import Emprestimo
from django import forms


# Classe de formatação de input do tipo date.
class DateInput(forms.DateInput):
    input_type = 'date'


# Formulário utilizado pra atualizar um empréstimo ja cadastrado no sistema.
class Alterar_Emprestimo(ModelForm):

    class Meta:
        model = Emprestimo
        fields = ('data_devolucao',)
        widgets = {
            'data_devolucao': DateInput(format='%Y-%m-%d')
        }


# Formulário utilizado para consultar os dados de um empréstimo já cadastrado no sistema.
class Consultar_Emprestimo(ModelForm):

    class Meta:
        model = Emprestimo
        fields = ('data_devolucao',)
        widgets = {
            'data_devolucao': DateInput(format='%Y-%m-%d')
        }
