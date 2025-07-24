CREATE TABLE IF NOT EXISTS cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    idade INTEGER,
    cep VARCHAR(10),
    saldo NUMERIC(12,2) DEFAULT 0.00,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table if not exists produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) not null, 
    quantidade INTEGER,
    valor INTEGER,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE IF NOT EXISTS transacoes (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES cliente(id),
    produto_id INTEGER NOT NULL REFERENCES produto(id),
    quantidade INTEGER not null,
    valor NUMERIC(12,2) NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cliente (nome, cpf, idade, cep, saldo) VALUES
  ('Alice Santos', '111.111.111-11', 28, '01001-000', 2000.00),
  ('Bruno Lima', '222.222.222-22', 35, '01002-000', 1200.00),
  ('Carla Mendes', '333.333.333-33', 42, '01003-000', 850.00),
  ('Daniel Souza', '444.444.444-44', 30, '01004-000', 1700.00);

INSERT INTO cliente (nome, cpf, idade, cep, saldo) VALUES
  ('Otávio Martins', '161.161.161-16', 41, '01015-000', 18500.00),
  ('Paula Rodrigues', '171.171.171-17', 36, '01016-000', 24250.75),
  ('Quésia Andrade', '181.181.181-18', 29, '01017-000', 32500.00),
  ('Renato Carvalho', '191.191.191-19', 52, '01018-000', 9800.40),
  ('Simone Guedes', '202.202.202-20', 47, '01019-000', 14120.00),
  ('Túlio Aguiar', '212.212.212-21', 33, '01020-000', 7750.00),
  ('Ursula Nunes', '222.222.222-23', 38, '01021-000', 30500.25),
  ('Vinícius Dantas', '232.232.232-24', 31, '01022-000', 8500.70),
  ('Weslley Cunha', '242.242.242-25', 39, '01023-000', 16450.00),
  ('Xênia Simões', '252.252.252-26', 27, '01024-000', 21700.00),
  ('Yiara Tomé', '262.262.262-27', 49, '01025-000', 38500.00),
  ('Zuleica Campos', '272.272.272-28', 44, '01026-000', 29900.90);

INSERT INTO cliente (nome, cpf, idade, cep, saldo) VALUES
  ('Eduarda Pires', '555.555.555-55', 26, '01005-000', 3200.50),
  ('Fábio Almeida', '666.666.666-66', 38, '01006-000', 950.00),
  ('Gabriela Torres', '777.777.777-77', 54, '01007-000', 4000.00),
  ('Henrique Castro', '888.888.888-88', 22, '01008-000', 500.00),
  ('Isabela Rocha', '999.999.999-99', 45, '01009-000', 2150.75),
  ('João Pedro Silva', '101.101.101-10', 31, '01010-000', 1420.30),
  ('Karen Lopes', '121.121.121-12', 27, '01011-000', 650.00),
  ('Lucas Ribeiro', '131.131.131-13', 24, '01012-000', 2700.00),
  ('Marina Fernandes', '141.141.141-14', 39, '01013-000', 1950.90),
  ('Nathalia Barros', '151.151.151-15', 34, '01014-000', 800.80);


INSERT INTO produto (nome, quantidade, valor) VALUES
  ('Notebook', 10, 3500),
  ('Mouse', 40, 100),
  ('Monitor', 15, 900),
  ('Teclado', 25, 250);

  INSERT INTO produto (nome, quantidade, valor) VALUES
  ('Headset Gamer', 18, 350),
  ('Impressora Laser', 7, 1200),
  ('Webcam HD', 28, 220),
  ('HD Externo 1TB', 12, 400),
  ('SSD 500GB', 25, 350),
  ('Pen Drive 64GB', 50, 60),
  ('Placa de Vídeo', 6, 2100),
  ('Memória RAM 16GB', 20, 380),
  ('Roteador Wi-Fi', 30, 200),
  ('Cadeira Gamer', 9, 1350),
  ('Microfone USB', 14, 175),
  ('Fonte 600W', 13, 290),
  ('Switch 8 portas', 10, 330),
  ('Tablet', 16, 1100),
  ('Projetor Multimídia', 5, 2600),
  ('Leitor de código de barras', 8, 420);

INSERT INTO transacoes (cliente_id, produto_id, quantidade, valor) VALUES
  (1, 1, 1, 3500.00), 
  (2, 2, 1, 100.00),  
  (3, 3, 1, 900.00),  
  (4, 4, 1, 250.00),  
  (1, 2, 1, 100.00);  


