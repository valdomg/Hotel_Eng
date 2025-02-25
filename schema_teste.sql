CREATE DATABASE IF NOT EXISTS hotel_teste;
USE hotel_teste;
#drop database hotel_teste;

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
    hotel_img_entrada VARCHAR (255),
    hotel_img_quarto VARCHAR (255),
    hotel_img_area_lazer VARCHAR (255),
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

INSERT INTO hoteis(nome, localizacao, hotel_img_entrada, hotel_img_quarto, hotel_img_area_lazer, descricao, categoria) VALUES
('Hotel Luxor', 'Rio de Janeiro, RJ', 'imagens/hoteis/hotel_luxor.png', 'imagens/hoteis/hotel_luxor.png', 'imagens/hoteis/hotel_luxor.png', 'Hotel de Luxo', 'luxo'),
('Pousada das Montanhas', 'Campos do Jordão, SP','imagens/hoteis/hotel_luxor.png' ,'imagens/hoteis/hotel_luxor.png','imagens/hoteis/hotel_luxor.png','Charmosa pousada nas montanhas.','pousada'),
('Resort Paraíso', 'Porto de Galinhas, PE', 'imagens/hoteis/hotel_luxor.png','imagens/hoteis/hotel_luxor.png','imagens/hoteis/hotel_luxor.png','Resort all-inclusive com piscinas naturais.', 'resort'),
('Hotel Econômico Centro', 'São Paulo, SP', 'imagens/hoteis/hotel_luxor.png','imagens/hoteis/hotel_luxor.png','imagens/hoteis/hotel_luxor.png','Opção acessível no centro da cidade.', 'econômico');


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
