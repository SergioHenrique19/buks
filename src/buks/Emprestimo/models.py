from django.db import models
from Livros.models import Livro
from Cliente.models import Cliente

# Create your models here.

class Emprestimo(models.Model):

    PAYMENT_CHOICES = {
        (0, 'Dinheiro'),
        (1, 'Cartão de Crédito/Débito'),
    }

    id_emprestimo = models.CharField(max_length=255, verbose_name="ID do Empréstimo", primary_key=True)
    data_emprestimo = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Data do Empréstimo", editable=True, help_text="Definido automaticamente após a confimação do empréstimo.")
    data_devolucao = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Data de Devolução")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Cliente")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, verbose_name="Livro")
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço Unitário")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade")
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")
    forma_pagamento = models.IntegerField(default=0, choices=PAYMENT_CHOICES, verbose_name="Forma de Pagamento")
    desconto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Desconto")
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor Total")

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return self.id_emprestimo
