# Sistema de Gerenciamento de Hospedagens

#  Nome do Projeto
Sistema de Gerenciamento de Hospedagens

##  Descrição do Problema e Solução Proposta
O problema abordado pelo projeto é a dificuldade dos usuários em encontrar, reservar e gerenciar hospedagens de maneira prática e eficiente. Muitos sistemas atuais são confusos e não oferecem uma boa experiência ao usuário.

A solução proposta é um sistema web intuitivo que permite aos usuários visualizar hotéis e residências disponíveis, adicionar hospedagens ao carrinho e realizar reservas com facilidade. O sistema também conta com um painel de usuário para gerenciar pedidos e um sistema de login seguro.

---

##  Tecnologias Utilizadas
- **Linguagem Back-end:** Python (Flask)
- **Banco de Dados:** MySQL
- **Front-end:** HTML, CSS (Grid), JavaScript
- **Gerenciamento de Pacotes:** pip, virtualenv
- **Autenticação:** Flask Session
- **Versionamento:** Git & GitHub

---

## **Instalação e Configuração**

##  Instruções de Instalação e Uso

###  Pré-requisitos
- Python 3 instalado
- MySQL instalado e configurado
- Gerenciador de pacotes `pip`


### **1. Clonar o Repositório**
```bash
git clone https://github.com/valdomg/Hotel_Eng.git
cd Hotel_Eng
```

### **2. Criar um Ambiente Virtual**
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

### **3. Instalar Flask**
```bash
pip install Flask
```

### **4. Instalar DotEnv, MySQlConnector e MySQLDB**
```bash
pip install flask-mysqldb
pip install flask-mysql-connector
pip install python-dotenv
```

### **5. Criar o Banco de Dados MYSQL**
1. Instale o MySQL e crie um banco de dados:
```bash
Copiar e colar o schema_teste.db e insert.db
```
2. Configure as credenciais no arquivo `.env` (crie este arquivo se não existir):
```ini
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_DATABASE=hotel_teste
SECRET_KEY=alguma_coisa
```

### **6. Executar o Servidor**
```bash
py app.py
```
```bash
python app.py
```
Acesse o sistema em `http://127.0.0.1:5000/`.

# Documentação da API Flask

## Visão Geral
Esta API em Flask gerencia um sistema de reservas de hospedagem, permitindo que usuários façam login, adicionem itens ao carrinho e visualizem informações sobre os hoteis e residências cadastradas.

## Configuração do Banco de Dados
A aplicação usa MySQL como banco de dados. As credenciais são carregadas a partir de variáveis de ambiente utilizando `dotenv`.

### Conexão com o MySQL
```python
MYSQL_CONNECTION = mysql.connector.connect(
    host= os.getenv('DB_HOST'),
    user= os.getenv('DB_USER'),
    password= os.getenv('DB_PASSWORD'),
    database= os.getenv('DB_DATABASE')
)
```

## Rotas da API

### 1. Home (`/`)
- **Método:** `GET`
- **Descrição:** Exibe a página inicial, listando todos os hoteis cadastrados.
- **Retorno:** Renderiza `index.html` com os dados dos hoteis.

### 2. Login (`/login`)
- **Método:** `GET, POST`
- **Descrição:** Permite que o usuário faça login na aplicação.
- **Entrada:** `email` e `senha` via `POST`.
- **Saída:** Redireciona para a home se autenticado, ou exibe mensagem de erro.

### 3. Página do Usuário (`/usuario/<int:id>`)
- **Método:** `GET`
- **Descrição:** Exibe os dados do usuário baseado no `id`.
- **Saída:** Renderiza `pageUsuario.html` com os dados do usuário.

### 4. Adicionar ao Carrinho (`/adicionar_carrinho`)
- **Método:** `POST`
- **Descrição:** Adiciona um item ao carrinho do usuário logado.
- **Entrada:** `hospedagem_id`, `quantidade`, `tipo_hospedagem`.
- **Saída:** JSON com mensagem de sucesso.

### 5. Remover do Carrinho (`/remover_carrinho/<int:item_id>`)
- **Método:** `DELETE`
- **Descrição:** Remove um item do carrinho baseado no `item_id`.
- **Saída:** JSON confirmando remoção.

### 6. Ver Carrinho (`/ver_carrinho`)
- **Método:** `GET`
- **Descrição:** Retorna os itens do carrinho do usuário.
- **Saída:** Renderiza `pageCarrinho.html` com os itens.

### 7. Logout (`/logout`)
- **Método:** `GET`
- **Descrição:** Remove os dados da sessão do usuário e redireciona para a home.

### 8. Página do Hotel (`/hotel/<int:id>`)
- **Método:** `GET`
- **Descrição:** Exibe detalhes de um hotel baseado no `id`.
- **Saída:** Renderiza `paginaHotel.html`.

### 9. Quem Somos (`/QuemSomos`)
- **Método:** `GET`
- **Descrição:** Exibe a página "Quem Somos".
- **Saída:** Renderiza `quemSomos.html`.

## Notas Finais
- O `session` é utilizado para gerenciar a autenticação dos usuários.
- As variáveis de ambiente devem ser definidas no `.env`.
- O `debug=True` está ativado para facilitar o desenvolvimento.


## 🤝 Como Contribuir
1. Faça um fork do projeto
2. Crie um branch para sua funcionalidade (`git checkout -b minha-funcionalidade`)
3. Faça commit das suas mudanças (`git commit -m 'Adicionei minha funcionalidade'`)
4. Envie para o repositório (`git push origin minha-funcionalidade`)
5. Abra um Pull Request

---

## 👥 Integrantes do Grupo
- **Paulo Braga** - Desenvolvedor
- **Valdemiro Gabriel** - Desenvolvedor
- **Yara Beatriz** - Desenvolvedor

Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato! 😃

