# Sistema de Gerenciamento de Hospedagens

Este é um sistema web para gerenciamento de hospedagens em hotéis, desenvolvido com Flask e MySQL.

## **Instalação e Configuração**

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

### **4. Instalar MySQlConnector**
```bash
pip install flask-mysql-connector
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
DB_NAME=hotel_teste
```

### **6. Executar o Servidor**
```bash
py app.py
```
Acesse o sistema em `http://127.0.0.1:5000/`.

## **Funcionalidades**
- Cadastro e login de usuários - a fazer
- Listagem de hotéis -  feito
- Gerenciamento de clientes - a fazer
- Sistema de reservas - a fazer
- Check-in e check-out - a fazer

