#importando módulo do SQlite
import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists morador (
                    cpf text,
                    nome text,
                    fone text,
                    email text,
                    guiche integer, 
                    id integer primary key autoincrement)""")
        self.conexao.commit()
        c.close()
