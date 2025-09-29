import sqlite3

#Função para inserir os valores
def inserir_dados(titulo, autor, ano):
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
            INSERT INTO livros (titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, ?)
            """, (titulo, autor, ano, "Sim"))

            print(f"Dados inseridos com sucesso!\nTITULO: {titulo}\nAUTOR: {autor}\nANO: {ano}")

    except Exception:
        print("O banco de dados está ocupado ou inacessível. Por favor, tente novamente mais tarde.")

#Função para listar livros 
def listar_livros(): 
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM livros")
            for linha in cursor.fetchall(): 
                print("-" * 25)
                print(f"\n10 > LISTA DE LIVROS\nID: {linha[0]} | TÍTULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIBILIDADE: {linha[4]}")
                print("-" * 25)

    except sqlite3.OperationalError:
        print("Não foi possivel acessar o banco de dados, verifique se o arquivo existe ou esta corrompido.")
    except Exception:
        print("O banco de dados está ocupado ou inacessível. Por favor, tente novamente mais tarde.") 

#Função de alteração de disponibilidade do livro
def disponibilidade_livros(titulo_livro):
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT disponivel FROM livros WHERE titulo = ?", (titulo_livro,))
            resultado = cursor.fetchone()
            if resultado is None:
                print("Nenhum livro encontrado com esse título.")
                return

            estado_atual = resultado[0]
            novo_estado = "Não" if estado_atual == "Sim" else "Sim"
            cursor.execute("UPDATE livros SET disponivel = ? WHERE titulo = ?", (novo_estado, titulo_livro))
            print(f"Disponibilidade do livro '{titulo_livro}' alterada para: {novo_estado}")
    except Exception:
        print("Erro ao atualizar disponibilidade.")


#Função para remover livros
def remover_livros(titulo_livro):
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM livros WHERE titulo = ?", (titulo_livro))
            if cursor.rowcount == 0:
                print(f"Nenhum livro encontrado com o nome: {titulo_livro} na tabela.")
            else:
                print(f"Livro com o nome: {titulo_livro} removido com sucesso.")

    except sqlite3.InterfaceError:
        print("O  informado é invalido, tente novamente.")
    except sqlite3.OperationalError:
        print("A tabela ainda não foi criada. Cadastre livros primeiro.")
    except Exception:
        print("Erro inexperado. Por favor, tente novamente mais tarde.")
    
    


    



    
    
