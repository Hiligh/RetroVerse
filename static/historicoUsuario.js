document.addEventListener("DOMContentLoaded", function() {

    document.querySelectorAll(".avaliacoes-list, .comentarios-list, .likes-list").forEach(list => {
        const items = Array.from(list.querySelectorAll("li"));
        items.slice(0, 4).forEach(item => item.classList.remove("d-none"));
    });

    function showMoreItems(listClass) {
        const items = document.querySelectorAll(`.${listClass} .d-none`);
        items.length > 0 && items.forEach((item, index) => {
            if (index < 4) item.classList.remove("d-none");
        });
        if (document.querySelectorAll(`.${listClass} .d-none`).length === 0) {
            document.querySelector(`button[data-target="${listClass}"]`).style.display = "none";
        }
    }

    document.querySelectorAll(".ver-mais").forEach(button => {
        button.addEventListener("click", function() {
            showMoreItems(button.getAttribute("data-target"));
        });
    });
});