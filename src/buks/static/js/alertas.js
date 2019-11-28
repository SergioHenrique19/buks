//Função para Enviar o formulário do registro do livro
function sendRegisterBook() {
  document.formResgisterBook.submit();
}

//Função para Enviar o formulário da alteração do livro
function sendUpdateBook() {
  document.formUpdateBook.submit();
}

//Função para Enviar o ISBN de deleção do livro
function sendDeleteBook() {
  document.formDeleteBook.submit();
}

//Função para Enviar o formulário do registro do Cliente
function sendRegisterClient() {
  document.formRegisterClient.submit();
}

//Função para Enviar o formulário do registro do Cliente
function sendUpdateClient() {
  document.formUpdateClient.submit();
}

//Tela de Sucesso do cadastro de Livro
function showSuccessRegisterBook() {
  Swal.fire({
    'title': 'Livro Cadastrado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

//Tela de Sucesso da deleção de Livro
function showSuccessDeleteBook() {
  Swal.fire({
    'title': 'Livro Excluído com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

//Tela de Sucesso da alteração de Livro
function showSuccessUpdateBook() {
  Swal.fire({
    'title': 'Livro Atualizado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

//Tela de Sucesso do cadastro de Cliente
function showSuccessRegisterClient() {
  Swal.fire({
    'title': 'Cliente Cadastrado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}

//Tela de Sucesso do cadastro de Cliente
function showSuccessUpdateClient() {
  Swal.fire({
    'title': 'Cliente Alterado com Sucesso!',
    'icon': 'success',
    'showCloseButton': false,
    'timer': 3000
  })
}
 