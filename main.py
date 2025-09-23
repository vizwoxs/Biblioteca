import sqlite3
import funcao

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

#Tabela de livros
cursor.execute("""
CREATE TABLE IF NOT EXIST livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER
    disponivel TEXT CHECK(disponivel IN ('Sim', 'Não')) NOT NULL)
""")



