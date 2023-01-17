class Produto:
    def __init__(self, nome, preco, marca=None, id=None, added=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.marca = marca
        self.added = added

class Cliente:
    def __init__(self, nome, email, id=None, cpf=None, cep=None, data_cadastro=None):
        """ Metodo construtor para cliente """
        # atributos obrigatorios:
        self.nome = nome
        self.email = email
        # atributos opcionais:
        self.id = id
        self.cpf = cpf
        self.cep = cep
        self.data_cadastro = data_cadastro

class ClienteProduto:
    def __init__(self, cliente_id, produto_id, id=None, added=None):
        self.id = id
        self.cliente_id = cliente_id
        self.produto_id = produto_id
        self.added = added