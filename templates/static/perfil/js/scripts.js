
function showProfile() {
    const mainContent = document.getElementById("main-content");
    mainContent.innerHTML = "<h2>Perfil</h2><p>Dados do usuário perfil.</p>";
}

function showSupporter() {
    const mainContent = document.getElementById("main-content");
    mainContent.innerHTML = "<h2>Apoiador</h2><p>Dados do usuário e feitos como apoiador.</p>";
}

function showVolunteer() {
    const mainContent = document.getElementById("main-content");
    mainContent.innerHTML = "<h2>Voluntário</h2><p>Dados do usuário e feitos como voluntário.</p>";
}

// Chamei a função showProfile() em js inicialmente para exibir os dados do perfil
showProfile();
