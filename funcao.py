import sqlite3

#Função para inserir os valores
def inserir_dados(titulo, autor, ano):
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano)
    VALUES (?, ?, ?, "Sim")
    """, (titulo, autor, ano))

    conexao.commit()
    conexao.close()

    print(f"Dados inseridos com sucesso!\nTITULO: {titulo}\nAUTOR: {autor}\nANO: {ano}")

