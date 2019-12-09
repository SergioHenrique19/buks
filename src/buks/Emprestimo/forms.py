from django.forms import ModelForm
from .models import Emprestimo
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class Alterar_Emprestimo(ModelForm):

    class Meta:
        model = Emprestimo
        fields = ('data_devolucao',)
        widgets = {
            'data_devolucao': DateInput(format='%Y-%m-%d')
        }


class Consultar_Emprestimo(ModelForm):

    class Meta:
        model = Emprestimo
        fields = ('data_devolucao',)
        widgets = {
            'data_devolucao': DateInput(format='%Y-%m-%d')
        }
