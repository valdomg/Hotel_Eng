CREATE DATABASE IF NOT EXISTS hotel_management;
USE hotel_management;
#drop database hotel_management;

-- Tabela de Usuários
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo ENUM('admin', 'funcionario') NOT NULL
);

-- Tabela de Hotéis
CREATE TABLE hoteis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    localizacao VARCHAR(255) NOT NULL,
    hotel_img integer,
    descricao TEXT,
    categoria ENUM('econômico', 'luxo', 'resort', 'pousada') NOT NULL
);

-- Tabela de Imagens de Hotéis
CREATE TABLE hotel_imagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT NOT NULL,
    caminho VARCHAR(255) NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hoteis(id) ON DELETE CASCADE
);

-- Tabela de Quartos
CREATE TABLE quartos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT NOT NULL,
    numero VARCHAR(10) NOT NULL,
    tipo ENUM('simples', 'duplo', 'suíte') NOT NULL,
    preco_diaria DECIMAL(10,2) NOT NULL,
    status ENUM('disponivel', 'ocupado', 'manutencao') NOT NULL DEFAULT 'disponivel',
    FOREIGN KEY (hotel_id) REFERENCES hoteis(id) ON DELETE CASCADE
);

-- Tabela de Imagens de Quartos
CREATE TABLE quarto_imagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quarto_id INT NOT NULL,
    caminho VARCHAR(255) NOT NULL,
    FOREIGN KEY (quarto_id) REFERENCES quartos(id) ON DELETE CASCADE
);

-- Tabela de Clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100) UNIQUE NOT NULL,
    documento VARCHAR(50) UNIQUE NOT NULL
);

-- Tabela de Reservas
CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    quarto_id INT NOT NULL,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    status ENUM('ativa', 'finalizada', 'cancelada') NOT NULL DEFAULT 'ativa',
    valor_total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
    FOREIGN KEY (quarto_id) REFERENCES quartos(id) ON DELETE CASCADE
);
