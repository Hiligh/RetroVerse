
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

document.getElementById('ativarAutenticacaoBtn').addEventListener('click', function() {
    fetch('/ativarAutenticacao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token() }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
        } else {
            alert('Erro ao ativar autenticação: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro. Tente novamente.');
    });
});
