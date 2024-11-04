let currentStep = 0;

const tutorialSteps = [
    {
        element: "#div-lateral img",
        text: "Clique na imagem de perfil para acessar o seu perfil de usuário."
    },
    {
        element: ".nav-item a[href='/paginaCatalogo']",
        text: "Clique em 'Catálogo' para visualizar todos os jogos disponíveis."
    },
    {
        element: ".nav-item a[href='/paginaForum']",
        text: "Clique em 'Fórum' para criar e comentar em tópicos com outros jogadores."
    },
    {
        element: ".nav-item a[href='/paginaGames']",
        text: "Clique em 'Biblioteca' para ver os jogos que você adicionou às suas listas."
    }
];

function checkTutorialStatus() {
    const tutorialStatus = localStorage.getItem("tutorialStatus");
    if (tutorialStatus === "skipped") {
        return;
    }

    const tutorialModal = new bootstrap.Modal(document.getElementById('tutorial-choice-modal'));
    tutorialModal.show();
}

function startTutorial() {
    currentStep = 0;
    const tutorialModal = bootstrap.Modal.getInstance(document.getElementById('tutorial-choice-modal'));
    tutorialModal.hide();
    document.getElementById("tutorial-overlay").classList.remove("d-none");
    showStep();
}

function skipTutorial() {

    localStorage.setItem("tutorialStatus", "skipped");
    const tutorialModal = bootstrap.Modal.getInstance(document.getElementById('tutorial-choice-modal'));
    tutorialModal.hide();
}

function showStep() {
    const { element, text } = tutorialSteps[currentStep];

    document.getElementById("tutorial-text").innerText = text;

    clearHighlights();
    const targetElement = document.querySelector(element);
    if (targetElement) {
        targetElement.classList.add("destaque");
        targetElement.style.zIndex = '1001';
        targetElement.style.position = 'relative';
        targetElement.scrollIntoView({ behavior: "smooth", block: "center" });
    }
}

function clearHighlights() {
    document.querySelectorAll(".destaque").forEach(el => {
        el.classList.remove("destaque");
        el.style.zIndex = '';
        el.style.position = '';
    });
}

function nextStep() {
    currentStep++;
    if (currentStep < tutorialSteps.length) {
        showStep();
    } else {
        endTutorial();
    }
}

function previousStep() {
    if (currentStep > 0) {
        currentStep--;
        showStep();
    }
}

function endTutorial() {
    clearHighlights();
    document.getElementById("tutorial-overlay").classList.add("d-none");
}

window.onload = checkTutorialStatus;
