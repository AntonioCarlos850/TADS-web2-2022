DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS produtos;

CREATE TABLE clientes(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cpf text NOT NULL,
    cep text NOT NULL,
    telefone text NOT NULL,
    senha text NOT NULL,
    data_nasc TIMESTAMP NOT NULL,
    email text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE produtos(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    marca text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO produtos (nome, marca)
VALUES ('arroz', 'sabor sul'), 
    ('feijao', 'sabor sul');

INSERT INTO clientes (nome, cpf, cep, telefone, senha, data_nasc,email)
VALUES
    ('admin','08695741235', '1002000','45998194884', '1234', 1054085801000, 'admin@test.org'),
    ('Maria Silver', '08695741235', '1002000','45998194884', '1234', 1054085801000, 'admin@test.org'),
    ('Jairo Carlile', '08695741235', '1002000','45998194884', '1234', 1054085801000, 'admin@test.org'),
    ('Marcos Oliva', '08695741235', '1002000','45998194884', '1234', 1054085801000, 'admin@test.org');