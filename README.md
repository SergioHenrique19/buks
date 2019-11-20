# Buks

Buks é um sistema de gerenciamento de livros, onde é possível cadastrar, atualizar, consultar e excluir registros de livros.

Além do gerenciamento de livros, objetivo principal, o usuário pode gerenciar suas compras e vendas, registros de clientes, de funcionários, de outros usuários e de fornecedores também, assim pode ser utilizado por livrarias, lojas de sebo, biblioteca ou algo que inclua tudo isso.

## Estrutura de diretório

Logo abaixo, confira a estrutura de diretório do sistema Buks:

```text
buks/
├──docs/
|  ├──padroes_adotados/
|  |  └──regras_de_verificacao_e_analise_de_requ
|  └──requisitos/
|     ├──interfaces/
|     ├──buks_documento_de_requisitos.doc
|     ├──buks_usecase_diagram.asta
|     ├──buks_usecase_diagram.png
|     ├──doc_requistos.md
|     └──prototipo_de_interfaces.md
├──src/
|  ├──buks/
|  |  ├──buks/
|  |  |  ├──__init__.py
|  |  |  ├──settings.py
|  |  |  ├──urls.py
|  |  |  └──wsgi.py
|  |  └──manage.py
|  └──.gitignore
└──README.md
```

A pasta "**src**" terá todo o código desenvolvido no projeto, enquanto a pasta "**docs**" terá todos os documentos necessários de Engenharia de Software e/ou que auxiliem na documentação do projeto.

## Tecnologias Utilizadas

* [HTML 5](https://www.w3schools.com/html/default.asp), [CSS 3](https://www.w3schools.com/css/) e [JavaScript](https://www.w3schools.com/js/default.asp) - principais linguagens utilizadas no desenvolvimento front-end
* [Django](https://www.djangoproject.com/) - web framework full-stack em Python
* [PostgreSQL](https://www.postgresql.org/) - sistema de gerenciamento de banco de dados com SQL

## Configuração das branches

Para o desenvolvimento será utilizado duas _branches_: **master** onde fica o projeto atualizado e em "produção", e **dev** utilizada principalmente pelos desenvolvedores, seja implementação e/ou testes.

## Configuração dos commits

- Usar modo imperativo ("Adiciona feature" não "Adicionando feature" ou "Adicionada feature")
- Primeira linha deve ter no máximo 72 caracteres
- Considere descrever com detalhes no corpo do commit
- Considere usar um emoji no início da mensagem de commit

Emoji | Code | Commit Type
------------ | ------------- | -------------
:tada: | `:tada:` | initial commit
:building_construction: | `:building_construction:` | quando melhorar a estrutura/formato do código
:hammer: | `:hammer:` | quando melhorar ou refatorar um código já existente
:memo: | `:memo:` | quando escrever alguma documentação
:bug: | `:bug:` | quando corrigir um bug
:heavy_check_mark: | `:heavy_check_mark:` | quando adicionar testes
:rocket: | `:rocket:` | nova feature
:arrow_up_down: | `:arrow_up_down:` | ao adicionar ou remover dependências.
:twisted_rightwards_arrows: | `:twisted_rightwards_arrows:` | merge em branchs
:rewind: | `:rewind:` | ao reverter versões
:whale: | `:whale:` | ao atualizar arquivos docker
:see_no_evil: | `:see_no_evil:` | gambiarra

[FONTE](https://gist.github.com/viniciustpimenta/c58ada969cf30130f74c2daebf4f15cb)

## Autores

* **Fábio Junio Rolin de Oliveira** - [FaBiUsKcomp](https://github.com/FaBiUsKcomp)
* **Otávio Augusto de Sousa Resende** - [otavio-resende98](https://github.com/otavio-resende98)
* **Sérgio Henrique Menta Garcia** - [SergioHenrique19](https://github.com/SergioHenrique19)
