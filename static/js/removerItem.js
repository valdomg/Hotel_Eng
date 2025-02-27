function removerItem(hotelId) {
    fetch(`/remover_carrinho/${hotelId}`, { method: "DELETE" })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status}`);
        }
        return response.json(); // Garantir que é um JSON válido
    })
    .then(data => {
        if (data.success) {
            alert(data.message); // Mensagem de sucesso
            location.reload(); // Atualiza a página automaticamente
        } else {
            alert("Erro ao remover o item: " + data.error);
        }
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Ocorreu um erro ao remover o item.");
    });
}
