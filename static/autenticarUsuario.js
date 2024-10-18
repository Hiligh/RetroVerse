function moveFocus(currentInput, nextInputId) {
    if (currentInput.value.length === 1) {
        document.getElementById(nextInputId).focus();
    }
}

function juntarCodigo() {
    const inputs = document.querySelectorAll('.input-box');
    let codigo = '';
    inputs.forEach(input => {
        codigo += input.value;
    });
    document.getElementById('codigo_verificacao').value = codigo;
}

document.querySelector('form').addEventListener('submit', juntarCodigo);