USE hotel_teste;
-- Inserções na tabela hoteis
INSERT INTO hoteis (nome, localizacao, preco_diaria, hotel_img_home, hotel_img_home_patrocinado, descricao, categoria) 
VALUES
('Hotel Paraíso Azul', 'Rio de Janeiro, RJ', 450.00, 'imagens/hoteis/paraiso_azul_home.jpg', 'imagens/patrocinado/paraiso_azul_patrocinado.jpg', 'Localizado à beira-mar, o Hotel Paraíso Azul oferece suítes confortáveis com vista panorâmica. Ideal para quem busca descanso e sofisticação.', 'Hotel de luxo'),

('Pousada Sol Nascente', 'Florianópolis, SC', 180.00, 'imagens/hoteis/sol_nascente_home.jpg', 'imagens/patrocinado/sol_nascente_patrocinado.jpg', 'A Pousada Sol Nascente combina charme e tranquilidade, com café da manhã incluso e acesso rápido às praias paradisíacas da região.', 'Hotel pousada'),

('Resort Tropical', 'Salvador, BA', 720.00, 'imagens/hoteis/resort_tropical_home.jpg', 'imagens/patrocinado/resort_tropical_patrocinado.jpg', 'Um resort cinco estrelas com piscinas, spa e atividades exclusivas. O local perfeito para férias inesquecíveis em um cenário tropical.', 'Hotel resort'),

('Econômico Centro', 'São Paulo, SP', 120.00, 'imagens/hoteis/economico_centro_home.jpg', 'imagens/patrocinado/economico_centro_patrocinado.jpg', 'Hospedagem acessível no centro de São Paulo, próxima a metrôs e pontos turísticos. Conforto e praticidade para sua viagem.', 'Hotel econômico'),

('Grand Palace', 'Gramado, RS', 650.00, 'imagens/hoteis/grand_palace_home.jpg', 'imagens/patrocinado/grand_palace_patrocinado.jpg', 'O Grand Palace é um hotel sofisticado na Serra Gaúcha, combinando luxo, gastronomia premiada e uma vista espetacular da natureza.', 'Hotel de luxo');

/*
-- Inserções na tabela residencia*/
INSERT INTO residencia (nome, localizacao, preco_diaria, residencia_img_home, residencia_img_home_patrocinado, descricao, categoria) 
VALUES
('Kame House', 'Oceano, Ilha', 0.00, 'imagens/residencias/kame-house.jpg', 'imagens/residencias/kame-house.jpg', 'A Kame House é uma pequena casa rosa em uma ilha isolada no oceano, lar do Mestre Kame em Dragon Ball.', 'Residência na Ilha'),

('Abacaxi Aquático', 'Fenda do Biquini, Oceano Pacífico', 20.00, 'imagens/residencias/abacaxi.jpg', 'imagens/residencias/abacaxi.jpg', 'A casa do Bob Esponja é um abacaxi gigante localizado no fundo do mar, na Fenda do Biquíni. Surpreendentemente espaçosa por dentro.', 'Casa Aquática'),

('Casa Sem Graça', 'Algum lugar, ES', 950.00, 'imagens/residencias/casa-sem-graca.jpg', 'imagens/residencias/casa-sem-graca.jpg', 'Uma casa sem graça é apenas um bloco de paredes sem vida. Sem decoração, cores vibrantes ou personalidade, ela parece fria e monótona', 'Casa'),

('Casa Simpsons', 'Springfield, TN', 80.00, 'imagens/residencias/casa-simpsons.jpg', 'imagens/residencias/casa-simpsons.jpg', 'A casa dos Simpsons, localizada no número 742 da Evergreen Terrace, é um ícone da cultura pop. Com sua fachada bege, telhado laranja e garagem lateral', 'Casa'),

('Casa Balão', 'Brasília, DF', 350.00, 'imagens/residencias/casa-up.jpg', 'imagens/residencias/casa-up.jpg',  'Com balões amarrados ao telhado, a casa se torna um meio para Carl realizar a aventura que sempre sonhou, voando para a América do Sul.', 'Casa com balão');


INSERT INTO users(nome, email, senha) VALUES 
('valdemiro', 'valdom123@gmail.com', '123');

INSERT INTO users(nome, email, senha) VALUES 
('gabriel', 'gabriel123@gmail.com', '123');




