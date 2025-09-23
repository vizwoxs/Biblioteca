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
def disponibilidade_livros(id_livros):
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livros))
            resultado = cursor.fetchone()
            if resultado is None:
                print("Nenhum livro encontrado")
                return
        
            estado_atual = resultado[0]
            novo_estado = "Não" if estado_atual == "Sim" else "Sim" #ternário
            cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo_estado, id_livros)) 
            print(f"Disponibilidade do livro ID: {id_livros} alterada para: {novo_estado}")

    except sqlite3.OperationalError:
        print("A tabela ainda não foi criada. Cadastre livros primeiro.")
    except sqlite3.InterfaceError:
        print("O ID informado é invalido, tente novamente.")
    except Exception:
        print("Erro inexperado. Por favor, tente novamente mais tarde.")

#Função para remover livros
def remover_livros(id_livros):
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM livros WHERE id = ?", (id_livros))
            if cursor.rowcount == 0:
                print(f"Nenhum livro encontrado com o ID: {id_livros} na tabela.")
            else:
                print(f"Livro com o ID: {id_livros} removido com sucesso.")

    except sqlite3.InterfaceError:
        print("O ID informado é invalido, tente novamente.")
    except sqlite3.OperationalError:
        print("A tabela ainda não foi criada. Cadastre livros primeiro.")
    except Exception:
        print("Erro inexperado. Por favor, tente novamente mais tarde.")
    
    


    



    
    
