function adicionarAoCarrinho(hospedagem_id, tipo_hospedagem) {
    fetch("/adicionar_carrinho", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            hospedagem_id: hospedagem_id,
            tipo_hospedagem: tipo_hospedagem  // Adicionando o tipo de hospedagem
        })
    })
    .then(response => response.json())
    .then(data => alert(data.mensagem))
    .catch(error => console.error("Erro:", error));
}
