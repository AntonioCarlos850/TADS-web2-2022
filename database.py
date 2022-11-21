import sqlite3


class Database():
    @staticmethod
    def create_db():
        """ Criar as tabelas """
        conn = sqlite3.connect('banco.db')
        with open('schema.sql') as f:
            # Executa o create table, insert, ...
            conn.executescript(f.read())
        conn.commit()
        conn.close()

    @staticmethod
    def get_connection():
        """ Obter uma conexão com o BD """
        conn = sqlite3.connect('banco.db')

        return conn
