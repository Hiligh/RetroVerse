document.addEventListener("DOMContentLoaded", function() {
    var erroMsgElement = document.getElementById("erro-msg");

    var erro = erroMsgElement ? erroMsgElement.textContent : null;

    if (erro) {
        alert(erro);
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const loginDiv = document.getElementById('div-login');
    loginDiv.classList.add('active');
});