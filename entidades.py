from datetime import datetime


class Cliente:
    def __init__(self, nome, cpf, cep, telefone, senha, data_nasc, email):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.telefone = telefone
        self.senha = senha
        self.data_nasc = data_nasc
        self.email = email


class Produto:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco
