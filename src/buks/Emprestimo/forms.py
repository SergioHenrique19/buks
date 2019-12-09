from django.forms import ModelForm
from .models import Emprestimo
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class Cadastro_Emprestimo(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Cadastro_Emprestimo, self).__init__(*args, **kwargs)
        self.fields['preco_unitario'].localize = True
        self.fields['preco_unitario'].widget.is_localized = True
        self.fields['valor'].localize = True
        self.fields['valor'].widget.is_localized = True
        self.fields['desconto'].localize = True
        self.fields['desconto'].widget.is_localized = True
        self.fields['valor_total'].localize = True
        self.fields['valor_total'].widget.is_localized = True

    class Meta:
        model = Emprestimo
        fields = '__all__'
        widgets = {
            'data_devolucao': DateInput(format='%Y-%m-%d')
        }


    