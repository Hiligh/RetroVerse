const senha = document.getElementById('criar-senha')
const confirmarSenha = document.getElementById('confirmar-senha')
const botaoCriarConta = document.getElementById('cadastro-button');

botaoCriarConta.addEventListener('click', function(event) {
    if (senha.value !== confirmarSenha.value) {
        event.preventDefault();
        
        //Trocar o alert pelo recurso do Bootstrap de notificação de erro.
        alert('As senhas não coincidem. Por favor, tente novamente.');
        senha.value = '';
        confirmarSenha.value = '';
    }
    if(verificaCaracteres(senha.value) == null){
        //Trocar o alert pelo recurso do Bootstrap de notificação de erro.
        alert('Coloque pelo menos 1 caractere especial na senha!');
        senha.value = '';
        confirmarSenha.value = '';
    }
});

const verificaCaracteres = (senha) => {
    const regex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
    return result = senha.match(regex);
}