from datetime import datetime


class Cliente:
    def __init__(self, id, nome, cpf, cep, telefone, senha, data_nasc, email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.telefone = telefone
        self.senha = senha
        self.data_nasc = data_nasc
        self.email = email
