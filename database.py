"""
Classe utilitária para 
ajudar na inicilização do 
banco de dados
"""
import csv, sqlite3

class Database:

    @staticmethod
    def create_db():
        """ criar as tabela """
        conn = sqlite3.connect('banco.db')
        print('Criando banco de dados...')
        with open('schema.sql') as f:
            # executa o create table, insert, ...
            conn.executescript(f.read())

        with open('lista-500.csv','r') as fin:
            dr = csv.DictReader(fin)
            to_db = [( i['nome'], i['marca'], i['preco']) for i in dr]

        cur = conn.cursor()
        cur.executemany("INSERT INTO produto (nome, marca, preco) VALUES (?, ?, ?);", to_db)
        conn.commit()
        conn.close()

    @staticmethod
    def get_connection():
        """ obter uma conexao com o BD """
        conn = sqlite3.connect('banco.db')
        return conn

if __name__ == '__main__':
    # descomentar linha abaixo para gerar o arquivo banco.db
    Database.create_db()
