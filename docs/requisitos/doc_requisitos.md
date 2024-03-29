# Especificação de Requisitos

## Requisitos Funcionais (RF)
| Identificação | [RF-001] Autenticar usuário |
|--|--|
| Casos de Uso Relacionados | **_CSU-001_** |
| Descrição | O sistema deverá ser capaz de autenticar usuário através do seu "**login**" e "**senha**", informados nos campos de mesmo nome. |

| Identificação | [RF-002] Cadastrar livro |
|--|--|
| Casos de Uso Relacionados | **_CSU-002_** |
| Descrição | O sistema deverá prover ao usuário _logado_  a opção de cadastrar um livro. Os campos a serem cadastrados são:<br><br><ul><li>ISBN</li><li>Capa</li><li>Título</li><li>Subtítulo</li><li>Autor</li><li>Editora</li><li>Edição</li><li>Ano</li><li>Nº de páginas</li><li>Quantidade</li><li>Gênero</li><li>Novo ou usuado (binário)</li><li>Sinopse</li><li>Preço de compra</li><li>Preço de venda</li></ul>|

| Identificação | [RF-003] Alterar livro |
|--|--|
| Casos de Uso Relacionados | **_CSU-003_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de alterar um livro cadastrado. Todos os campos poderão ser alterados. |

| Identificação | [RF-004] Consultar livro  |
|--|--|
| Casos de Uso Relacionados | **_CSU-004_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de consultar um livro ou vários pelo campo "título". |

| Identificação | [RF-005] Excluir livro |
|--|--|
| Casos de Uso Relacionados | **_CSU-005_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de excluir um livro ou mais a partir da busca filtrada correspondente a um dos campos do registro do mesmo. |

| Identificação | [RF-006] Emprestar livro |
|--|--|
| Casos de Uso Relacionados | **_CSU-006_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de realizar o empréstimo de um livro ou mais para um cliente. Os campos a serem cadastrados são:<br><br><ul><li>ID</li><li>Data e hora</li><li>Data de devolução</li><li>Cliente</li><li>Livro(s)</li><li>Preço unitário</li><li>Quantidade(s)</li><li>Valor</li><li>Forma de pagamento</li><li>Desconto</li><li>Valor total</li></ul> |

| Identificação | [RF-007] Alterar empréstimo |
|--|--|
| Casos de Uso Relacionados | **_CSU-007_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de alterar um empréstimo cadastrado/registrado. Os seguintes campos podem ser alterados: "data de devolução", "quantidade" e "desconto". |

| Identificação | [RF-008] Consultar empréstimo |
|--|--|
| Casos de Uso Relacionados | **_CSU-008_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de consultar um empréstimo ou vários pelo campo "ID". |

| Identificação | [RF-009] Excluir empréstimo |
|--|--|
| Casos de Uso Relacionados | **_CSU-009_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de excluir um empréstimo ou mais a partir da busca filtrada correspondente a um dos campos do registro do mesmo. |

| Identificação | [RF-010] Comprar livro |
|--|--|
| Casos de Uso Relacionados | **_CSU-010_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de realizar uma compra de um ou mais livros. Os campos a serem cadastrados são:<br><br><ul><li>ID</li><li>Data</li><li>Fornecedor</li><li>Livro</li><li>Preço unitário</li><li>Quantidade</li><li>Preço total</li><li>Subtotal</li><li>Desconto</li><li>Total</li></ul> |

| Identificação | [RF-011] Consultar compra |
|--|--|
| Casos de Uso Relacionados | **_CSU-011_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de uma compra ou vários pelos filtros: ID, data, fornecedor, total. |

| Identificação | [RF-012] Cadastrar cliente |
|--|--|
| Casos de Uso Relacionados | **_CSU-012_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de cadastrar cliente. Os campos a serem cadastrados são:<br><br><ul><li>CPF</li><li>Nome</li><li>Data de nascimento</li><li>E-mail</li><li>Celular</li></ul> |

| Identificação | [RF-013] Alterar cliente |
|--|--|
| Casos de Uso Relacionados | **_CSU-013_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de alterar um cliente cadastrado. Todos os campos podem ser alterados. |

| Identificação | [RF-014] Consultar cliente |
|--|--|
| Casos de Uso Relacionados | **_CSU-014_** |
| Descrição | O sistema deverá prover ao usuário _logado_ a opção de consultar um cliente ou vários pelo campo "e-mail". |

## Requisitos Não-Funcionais (RNF)

| Identificação | [RNF-001] Funcionamento do sistema offline |
|--|--|
| Categoria | Disponibilidade |
| Descrição | O sistema deverá funcionar com ou sem conexão à rede. |

| Identificação | [RNF-002] Tela de confirmação |
|--|--|
| Categoria | Padrão |
| Descrição | O sistema deverá aprensentar uma tela de confirmação após o usuário realizar qualquer ação que envolva cadastros, alterações e exclusões. |

| Identificação | [RNF-003] Ambiente de execução |
|--|--|
| Categoria | Padrão |
| Descrição | O sistema será construído para rodar em ambiente web. |

| Identificação | [RNF-004] Compatibilidade com navegadores Chrome e Firefox |
|--|--|
| Categoria | Usabilidade |
| Descrição | O sistema deverá ser compatível para ser utilizado nos navegadores Google Chrome (a partir da versão 70) e Mozilla Firefox (a partir da versão 60). |
