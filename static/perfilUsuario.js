//Ao apertar no botão dele, ele usa a rota de /excluirConta para excluir os dados do usuário no banco de dados.
document.getElementById('confirmDelete').addEventListener('click', function() {

    fetch('/excluirConta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token() }}'
        }
    })
    .then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        } else {
            alert('Erro ao excluir a conta. Tente novamente.');
        }
    })
    .catch(error => console.error('Erro:', error));
});