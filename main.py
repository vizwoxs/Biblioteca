import sqlite3
import funcao as fun

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# Tabela de livros
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT CHECK(disponivel IN ('Sim', 'Não')) NOT NULL
)
""")

# Menu console
while True:
    print()
    print('-' * 35)
    print("Bem-vindo à nossa biblioteca SENAI")
    print("1. Cadastrar livro\n2. Listar livros\n3. Atualizar disponibilidade\n4. Remover livro\n5. Sair")
    print('-' * 35)
    escolha = int(input("Escolha uma das opções acima: "))
    print('-' * 35)

    if escolha == 5:
        break

    elif escolha == 1:
        print("Cadastrar livro")        
        print("-" * 35)
        titulo = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de lançamento do livro: ")
        print("-" * 35)

    elif escolha == 2:
        lista = fun.listar_livros()

    elif escolha == 3:
        print("-" * 35)
        titulo = input("Digite o nome do livro: ").strip()
        fun.disponibilidade_livros(titulo)

    elif escolha == 4:
        print("-" * 35)
        excluir = input("Digite o nome do livro que deseja excluir: ").strip()
        fun.remover_livros(excluir)





