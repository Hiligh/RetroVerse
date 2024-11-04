
const stars = document.querySelectorAll('.star');
const ratingValue = document.getElementById('rating-value');
let selectedRating = 0;

stars.forEach((star, index) => {
    star.addEventListener('click', function() {
        selectedRating = index + 1;
        ratingValue.textContent = selectedRating;

        stars.forEach(s => s.classList.remove('selected'));
        

        stars.forEach((s, i) => {
            if (i < selectedRating) {
                s.classList.add('selected');
            }
        });
    });
});

document.getElementById('submit-rating').addEventListener('click', function() {
    if (selectedRating > 0) {
        const jogoId = document.getElementById('jogo-id').value;
        fetch('/avaliarJogo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                jogo_id: jogoId,
                rating: selectedRating
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Avaliação enviada com sucesso!');
            } else {
                alert('Erro ao enviar a avaliação.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao enviar a avaliação. Tente novamente mais tarde.');
        });
    } else {
        alert('Selecione uma nota!');
    }
});

document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', function(event) {
        const listaNome = event.target.textContent;
        const jogoId = document.getElementById('jogo-id').value;

        fetch('/adicionarJogosLista', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ jogo_id: jogoId, lista_nome: listaNome })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
            } else if (data.error) {
                alert(data.error);
            }
        })
        .catch(error => console.error('Erro:', error));
    });
});

document.getElementById('message-container').textContent = data.message || data.error;

