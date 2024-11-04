const searchInput = document.getElementById('searchInput');
const suggestionsDropdown = document.getElementById('suggestionsDropdown');

searchInput.addEventListener('input', function() {
    const query = this.value.trim();

    if (query.length > 2) {

        fetch('/dropdownCatalogo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ search_term: query }),
            credentials: 'same-origin'
        })
        .then(response => response.json())
        .then(data => {

            suggestionsDropdown.innerHTML = '';
            if (data.suggestions && data.suggestions.length > 0) {
                data.suggestions.forEach(suggestion => {
                    const suggestionItem = document.createElement('li');
                    suggestionItem.classList.add('dropdown-item');
                    suggestionItem.textContent = suggestion;

                    suggestionItem.addEventListener('click', function() {
                        searchInput.value = suggestion;
                        suggestionsDropdown.innerHTML = '';
                        suggestionsDropdown.style.display = 'none';
                    });

                    suggestionsDropdown.appendChild(suggestionItem);
                });
                suggestionsDropdown.style.display = 'block';
            } else {
                const noResultItem = document.createElement('li');
                noResultItem.classList.add('dropdown-item', 'disabled');
                noResultItem.textContent = 'Nenhum resultado encontrado';
                suggestionsDropdown.appendChild(noResultItem);
                suggestionsDropdown.style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Erro ao buscar sugestões:', error);
        });
    } else {
        suggestionsDropdown.innerHTML = '';
        suggestionsDropdown.style.display = 'none';
    }
});

document.addEventListener('click', function(event) {
    if (!searchInput.contains(event.target) && !suggestionsDropdown.contains(event.target)) {
        suggestionsDropdown.style.display = 'none';
    }
});
