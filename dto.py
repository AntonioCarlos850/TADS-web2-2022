from database import Database
from entidades import Cliente, Produto


class ClienteDto:
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


class ProdutoDto:
    def save(self, produto: Produto):
        conn = Database.get_connection()
        conn.execute(
            "INSERT INTO produtos (nome, marca) VALUES (?, ?)",
            (produto.nome, produto.marca))
        conn.commit()
        conn.close()

    def all(self):
        conn = Database.get_connection()
        res = conn.execute("SELECT * FROM produtos")
        return res.fetchall()


if __name__ == '__main__':
    Database.create_db()
    produto = Produto("teste", "marca teste")
    dto = ProdutoDto()
    dto.save(produto)
    res = dto.all()
    print(res)

    cliente = Cliente("nome do cliente", "78965412300",
                      "85856350", "45988552234", "9874", 1054085801000, "antoniocarlos@gmail.com")
    clienteDto = ClienteDto()
    clienteDto.save(cliente)
    res = clienteDto.all()
    print(res)
