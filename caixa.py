import sqlite3
from sqlite3 import Error

# --------------------- Classe Banco de dados ----------------------
class Banco():
    def conecta_banco(self):
        self.conexao = sqlite3.connect('bancodedados.bd')
        self.sql = self.conexao.cursor()
        print('Banco de dados ativado!')

    def desconecta_banco(self):
        self.conexao.close()
        print('Banco de dados desconectado!')

    def criar_tabela(self):
        self.conecta_banco()
        try:
            self.sql.execute('''
                CREATE TABLE IF NOT EXISTS 
                hospedes (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome_hospede VARCHAR(50) NOT NULL,
                          email_hospede VARCHAR(50) NOT NULL,
                          cpf_hospede VARCHAR(11) NOT NULL,
                          contato_hospede VARCHAR(30) NOT NULL,
                          quarto_hospede VARCHAR(10), 
                          data_hospede VARCHAR(8))     
            ''')
            self.conexao.commit()
            print('Tabela criada com sucesso!')
            self.desconecta_banco()
        except Error:
            print('Ocorreu erro!', Error)