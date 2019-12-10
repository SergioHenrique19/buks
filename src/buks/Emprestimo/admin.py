from django.contrib import admin
from .models import Emprestimo

# Register your models here.

class EmprestimoAdmin(admin.ModelAdmin):

    readonly_fields = ['data_emprestimo']

    # The fields in the order you want them
    fieldsets = (
        (None, {
            'fields': ('id_emprestimo', 'data_emprestimo', 'data_devolucao',
                        'cliente', 'livro', 'preco_unitario', 'quantidade',
                        'valor', 'forma_pagamento', 'desconto', 'valor_total',)
        }),
    )

admin.site.register(Emprestimo, EmprestimoAdmin)
