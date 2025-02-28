document.getElementById('redefinirSenhaForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Evita o envio tradicional do formulário
    
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;

    // Enviar a requisição para o servidor com fetch
    fetch('/definir-senha', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, senha: senha })
    })
    .then(response => response.text())
    .then(data => {
        alert(data);  // Exibe uma mensagem com a resposta do servidor
        window.location.href = '/';  // Redireciona para a página inicial ou outra página
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao tentar redefinir a senha.');
    });
});
