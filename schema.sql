CREATE DATABASE IF NOT EXISTS hotel_teste;
USE hotel_teste;
#drop database hotel_teste;

-- Tabela de Usuários
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE admins(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

-- Tabela de Hotéis
CREATE TABLE hoteis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    localizacao VARCHAR(255) NOT NULL,
    preco_diaria DECIMAL(5,2),
    
    hotel_img_home VARCHAR (255) ,
    hotel_img_home_patrocinado VARCHAR (255) ,
    
    descricao TEXT NOT NULL,
    categoria ENUM('Hotel econômico', 'Hotel de luxo', 'Hotel resort', 'Hotel pousada') NOT NULL
);

-- Tabela de Residências
CREATE TABLE residencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    localizacao VARCHAR(255) NOT NULL,
    preco_diaria DECIMAL(5,2),
    
    residencia_img_home VARCHAR (255) ,
    residencia_img_home_patrocinado VARCHAR (255) ,
    
    descricao TEXT NOT NULL,
    categoria ENUM('Residência na Ilha', 'Casa Aquática', 'Casa', 'Casa com balão', 'Flat') NOT NULL
);

CREATE TABLE reserva_hotel(
	id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    hotel_id INT NOT NULL,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    preco_total DECIMAL(5,2),
    status ENUM('ativa', 'finalizada', 'cancelada') NOT NULL DEFAULT 'ativa',
    valor_total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (hotel_id) REFERENCES hoteis(id) ON DELETE CASCADE
);

CREATE TABLE reserva_residencia(
	id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    residencia_id INT NOT NULL,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    preco_total DECIMAL(5,2),
    status ENUM('ativa', 'finalizada', 'cancelada') NOT NULL DEFAULT 'ativa',
    valor_total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (residencia_id) REFERENCES residencia(id) ON DELETE CASCADE
);

CREATE TABLE carrinho (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    hospedagem_id INT NOT NULL,
    tipo_hospedagem ENUM('hotel', 'residencia') NOT NULL, -- Define se é um hotel ou residência
    quantidade INT DEFAULT 1,
    preco_total DECIMAL(10,2),
    data_adicionado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES users(id)
);




