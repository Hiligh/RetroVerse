document.addEventListener("DOMContentLoaded", function() {
    // Captura o elemento div que contém a mensagem de erro
    var erroMsgElement = document.getElementById("erro-msg");
    
    // Pega o texto contido no elemento
    var erro = erroMsgElement ? erroMsgElement.textContent : null;
    
    // Se houver uma mensagem de erro, exibe o alerta
    if (erro) {
        alert(erro);
    }
});