"""
Dao - Data access object
Implementa a conexao com o
banco de dados.

"""
from database import Database
from entidades import Cliente, Produto

class ProdutoDao:
    def save(self, produto):
        """
        Realiza o INSERT na tabela produto
        """
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO produto (
                nome, preco, marca           
            ) VALUES (?, ?, ?)
            """,
            (
                produto.nome,  
                produto.preco, 
                produto.marca,
            )
        )
        conn.commit()
        conn.close()


    def update(self, produto):
        """
        Realiza UPDATE do produto
        """
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE produto SET nome = ?, preco = ?, marca = ?
            WHERE id = ?
            """,
            (
                produto.nome,
                produto.preco,
                produto.marca,
                produto.id
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        """
        Remove um produto de acordo com o id fornecido
        """
        conn = Database.get_connection()
        conn.execute(
            # Query
            # Hard Delete (cuidado!)
            f"""
            DELETE FROM produto WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()


    def find_all(self, search=""):
        conn = Database.get_connection()
        res = conn.execute(
            f"""
            SELECT id, nome, preco, marca, added FROM produto 
            WHERE produto.nome LIKE \"%{search}%\"
            """
        )
        # executa o SELECT
        results = res.fetchall()
        # results eh um vetor

        # versao 1
        results = [
            { 
                "id": produto[0], 
                "nome": produto[1],
                "preco": produto[2],
                "marca": produto[3],
                "added": produto[4],
            } for produto in results]

        conn.close()
        return results


    def get_produto(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, preco, marca, added FROM produto WHERE id = {id}
        """
        )
        row = res.fetchone()
        
        # cria um objeto produto para armazenar resultado do SELECT:
        produto = Produto( 
            row[1],
            row[2],
            id = row[0],
            marca = row[3],
            added = row[4],
        )
        conn.close()
        return produto

    def count(self, search=""):
        conn = Database.get_connection()
        res = conn.execute(
            f"""
            SELECT COUNT(id) FROM produto 
            WHERE produto.nome LIKE \"%{search}%\"
            """
        )
        # executa o SELECT
        results = res.fetchone()
        # results eh um vetor

        conn.close()
        return results[0]

class ClienteDao:

    def save(self, cliente):
        """
        Realiza o INSERT na tabela cliente
        """
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (
                nome, cpf, cep, email            
            ) VALUES (?, ?, ?, ?)
            """,
            (
                cliente.nome,  
                cliente.cpf, 
                cliente.cep,
                cliente.email, 
            )
        )
        conn.commit()
        conn.close()


    def update(self, cliente):
        """
        Realiza UPDATE do cliente
        """
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE cliente SET nome = ?, cpf = ?, cep = ?, email = ?
            WHERE id = ?
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email,
                cliente.id
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        """
        Remove um cliente de acordo com o id fornecido
        """
        conn = Database.get_connection()
        conn.execute(
            # Query
            # Hard Delete (cuidado!)
            f"""
            DELETE FROM cliente WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()


    def find_all(self, search=""):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, cpf, cep, email, data_cadastro FROM cliente
        WHERE nome LIKE \"%{search}%\"
        """
        )
        # executa o SELECT
        results = res.fetchall()
        # results eh um vetor

        # versao 1
        results = [
            { 
                "id": cliente[0], 
                "nome": cliente[1],
                "cpf": cliente[2],
                "cep": cliente[3],
                "email": cliente[4],
                "data_cadastro": cliente[5],
            } for cliente in results]

        conn.close()
        return results


    def get_cliente(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, email, cpf, cep, data_cadastro  FROM cliente WHERE id = {id}
        """
        )
        row = res.fetchone()
        
        # cria um objeto cliente para armazenar resultado do SELECT:
        cliente = Cliente( 
            row[1],
            row[2],
            id = row[0],
            cpf = row[3],
            cep = row[4],             
            data_cadastro = row[5]
        )
        conn.close()
        return cliente

    def count(self, search=""):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT COUNT(id) FROM cliente
        WHERE nome LIKE \"%{search}%\"
        """
        )
        # executa o SELECT
        results = res.fetchone()
        # results eh um vetor

        conn.close()
        return results[0]

class ClienteProdutoDao:
    def save(self, cliente_produto):
        """
        Realiza o INSERT na tabela cliente_produto
        """
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente_produto (
                cliente_id, produto_id           
            ) VALUES (?, ?)
            """,
            (
                cliente_produto.cliente_id,  
                cliente_produto.produto_id,
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        """
        Remove um produto de acordo com o id fornecido
        """
        conn = Database.get_connection()
        conn.execute(
            # Query
            # Hard Delete (cuidado!)
            f"""
            DELETE FROM cliente_produto WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()


    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute(
            f"""
            SELECT cliente_produto.id, 
                cliente.nome as cliente_nome, 
                produto_id,
                produto.nome as produto_nome,
                produto.marca as produto_marca,
                produto.preco as produto_preco,
                cliente_produto.added
            FROM cliente_produto
                INNER JOIN cliente ON cliente.id = cliente_produto.cliente_id
                INNER JOIN produto ON produto.id = cliente_produto.produto_id
            """
        )
        # executa o SELECT
        results = res.fetchall()
        # results eh um vetor

        # versao 1
        results = [
            { 
                "id": cliente_produto[0], 
                "cliente_nome": cliente_produto[1],
                "produto_id": cliente_produto[2],
                "produto_nome": cliente_produto[3],
                "produto_marca": cliente_produto[4],
                "produto_preco": cliente_produto[5],
                "added": cliente_produto[6],
            } for cliente_produto in results]

        conn.close()
        return results

    def count(self):
        conn = Database.get_connection()
        res = conn.execute(
            f"""
            SELECT COUNT(id) FROM cliente_produto
            """
        )
        # executa o SELECT
        results = res.fetchone()
        # results eh um vetor

        conn.close()
        return results[0]
