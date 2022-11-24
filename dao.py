from database import Database
from entidades import Cliente, Produto


class ClienteDao:
    def __init__(self) -> None:
        pass

    def save(self, cliente: Cliente):
        conn = Database.get_connection()
        conn.execute(
            "INSERT INTO clientes (nome, cpf, cep, telefone, senha, data_nasc, email) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (cliente.nome, cliente.cpf, cliente.cep, cliente.telefone, cliente.senha, cliente.data_nasc, cliente.email))
        conn.commit()
        conn.close()

    def all(self):
        conn = Database.get_connection()
        res = conn.execute("SELECT * FROM clientes")
        return res.fetchall()


class ProdutoDao:
    def save(self, produto: Produto):
        conn = Database.get_connection()
        conn.execute(
            "INSERT INTO produtos (nome, marca, preco) VALUES (?, ?, ?)",
            (produto.nome, produto.marca, produto.preco))
        conn.commit()
        conn.close()

    def all(self):
        conn = Database.get_connection()
        res = conn.execute("SELECT * FROM produtos")
        return res.fetchall()


if __name__ == '__main__':
    Database.create_db()
    dao = ProdutoDao()
    res = dao.all()
    print(res)

    clienteDao = ClienteDao()
    res = clienteDao.all()
    print(res)
