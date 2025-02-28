function pesquisarItem(termo) {
    fetch("/pesquisar", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            termo: termo,
              
        })
    })
    .then(response => response.json())
    .then(data => alert(data.mensagem))
    .catch(error => console.error("Erro:", error));
}
