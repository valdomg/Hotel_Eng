-- Inserções na tabela hoteis
INSERT INTO hoteis (nome, localizacao, preco_diaria, hotel_img_home, hotel_img_home_patrocinado, hotel_img_page_hotelhotel_img_page_hotel, hotel_img_quarto, hotel_img_area_lazer, descricao, categoria) 
VALUES
('Hotel Paraíso Azul', 'Rio de Janeiro, RJ', 450.00, 'imagens/hoteis/paraiso_azul_home.jpg', 'imagens/patrocinado/paraiso_azul_patrocinado.jpg', 'imagens/quarto/paraiso_azul_page.jpg', 'imagens/area_lazer/paraiso_azul_quarto.jpg', 'paraiso_azul_lazer.jpg', 'Localizado à beira-mar, o Hotel Paraíso Azul oferece suítes confortáveis com vista panorâmica. Ideal para quem busca descanso e sofisticação.', 'Hotel de luxo'),

('Pousada Sol Nascente', 'Florianópolis, SC', 180.00, 'imagens/hoteis/sol_nascente_home.jpg', 'imagens/patrocinado/sol_nascente_patrocinado.jpg', 'imagens/quarto/sol_nascente_page.jpg', 'imagens/area_lazer/sol_nascente_quarto.jpg', 'sol_nascente_lazer.jpg', 'A Pousada Sol Nascente combina charme e tranquilidade, com café da manhã incluso e acesso rápido às praias paradisíacas da região.', 'Hotel pousada'),

('Resort Tropical', 'Salvador, BA', 720.00, 'imagens/hoteis/resort_tropical_home.jpg', 'imagens/patrocinado/resort_tropical_patrocinado.jpg', 'imagens/quarto/resort_tropical_page.jpg', 'imagens/area_lazer/resort_tropical_quarto.jpg', 'resort_tropical_lazer.jpg', 'Um resort cinco estrelas com piscinas, spa e atividades exclusivas. O local perfeito para férias inesquecíveis em um cenário tropical.', 'Hotel resort'),

('Econômico Centro', 'São Paulo, SP', 120.00, 'imagens/hoteis/economico_centro_home.jpg', 'imagens/patrocinado/economico_centro_patrocinado.jpg', 'imagens/quarto/economico_centro_page.jpg', 'imagens/area_lazer/economico_centro_quarto.jpg', 'economico_centro_lazer.jpg', 'Hospedagem acessível no centro de São Paulo, próxima a metrôs e pontos turísticos. Conforto e praticidade para sua viagem.', 'Hotel econômico'),

('Grand Palace', 'Gramado, RS', 650.00, 'imagens/hoteis/grand_palace_home.jpg', 'imagens/patrocinado/grand_palace_patrocinado.jpg', 'imagens/quarto/grand_palace_page.jpg', 'imagens/area_lazer/grand_palace_quarto.jpg', 'grand_palace_lazer.jpg', 'O Grand Palace é um hotel sofisticado na Serra Gaúcha, combinando luxo, gastronomia premiada e uma vista espetacular da natureza.', 'Hotel de luxo');

/*
-- Inserções na tabela residencia
INSERT INTO residencia (nome, localizacao, preco_diaria, residencia_img_home, residencia_img_home_patrocinado, residencia_img_quarto, residencia_img_fachada, residencia_img_area_lazer, descricao, categoria) 
VALUES
('Casa da Praia', 'Ubatuba, SP', 380.00, 'casa_praia_home.jpg', 'casa_praia_patrocinado.jpg', 'casa_praia_quarto.jpg', 'casa_praia_fachada.jpg', 'casa_praia_lazer.jpg', 'Uma casa espaçosa a poucos metros do mar, perfeita para relaxar e aproveitar o som das ondas. Acomoda até 8 pessoas.', 'Residência na praia'),

('Cobertura Panorâmica', 'Balneário Camboriú, SC', 920.00, 'cobertura_home.jpg', 'cobertura_patrocinado.jpg', 'cobertura_quarto.jpg', 'cobertura_fachada.jpg', 'cobertura_lazer.jpg', 'Apartamento de alto padrão com vista incrível da cidade e do mar. Oferece piscina privativa e amplo espaço para lazer.', 'Apartamento'),

('Bangalô Encantado', 'Ilhabela, SP', 500.00, 'bangalo_home.jpg', 'bangalo_patrocinado.jpg', 'bangalo_quarto.jpg', 'bangalo_fachada.jpg', 'bangalo_lazer.jpg', 'Rústico e aconchegante, este bangalô está rodeado pela natureza e oferece total privacidade. Ideal para quem busca tranquilidade.', 'Bangalô'),

('Sobrado Conforto', 'Curitiba, PR', 280.00, 'sobrado_home.jpg', 'sobrado_patrocinado.jpg', 'sobrado_quarto.jpg', 'sobrado_fachada.jpg', 'sobrado_lazer.jpg', 'Um sobrado moderno com três quartos, cozinha completa e espaço para churrasco. Perfeito para viagens em família.', 'Sobrado'),

('Flat Executivo', 'Brasília, DF', 350.00, 'flat_home.jpg', 'flat_patrocinado.jpg', 'flat_quarto.jpg', 'flat_fachada.jpg', 'flat_lazer.jpg', 'Flat mobiliado no centro de Brasília, ideal para estadias curtas e longas. Inclui serviço de limpeza e estacionamento.', 'Flat');
*/

/*Inserção de usuários*/
INSERT INTO users(nome, email, senha) VALUES 
('valdemiro', 'valdom123@gmail.com', '123');

INSERT INTO users(nome, email, senha) VALUES 
('gabriel', 'gabriel123@gmail.com', '123');