import sqlite3


#Função para inserir os valores
def inserir_dados(titulo, autor, ano):
    with sqlite3.connect("biblioteca.db") as conexao:
        cursor = conexao.cursor

    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano)
    VALUES (?, ?, ?, "Sim")
    """, (titulo, autor, ano))

    conexao.commit()

    print(f"Dados inseridos com sucesso!\nTITULO: {titulo}\nAUTOR: {autor}\nANO: {ano}")

#Função para listar livros 
def listar_livros(id, titulo, autor, ano, disponivel):
    with sqlite3.connect("biblioteca.db") as conexao:
        cursor = conexao.cursor
    try:
        for linha in cursor.fetchall():
            print("-" * 25)
            print(f"\n10 > LISTA DE LIVROS\nID: {linha[0]} | TÍTULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIBILIDADE: {linha[4]}")
            print("-" * 25)
    except sqlite3.OperationalError:
        print("Não foi possivel acessar o banco de dados, verifique se o arquivo existe ou esta corrompido.")
    except Exception:
        print("O banco de dados está ocupado ou inacessível. Por favor, tente novamente mais tarde.")


    
