import sqlite3


#Função para inserir os valores
def inserir_dados(titulo, autor, ano):
    with sqlite3.connect("biblioteca.db") as conexao:
        cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano)
    VALUES (?, ?, ?, "Sim")
    """, (titulo, autor, ano))

    conexao.commit()

    print(f"Dados inseridos com sucesso!\nTITULO: {titulo}\nAUTOR: {autor}\nANO: {ano}")

#Função para listar livros 
def listar_livros(): 
    with sqlite3.connect("biblioteca.db") as conexao:
        cursor = conexao.cursor
    try:
        for linha in cursor.fetchall(): #colocar a conexao do commit
            print("-" * 25)
            print(f"\n10 > LISTA DE LIVROS\nID: {linha[0]} | TÍTULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIBILIDADE: {linha[4]}")
            print("-" * 25)
    except sqlite3.OperationalError:
        print("Não foi possivel acessar o banco de dados, verifique se o arquivo existe ou esta corrompido.")
    except Exception:
        print("O banco de dados está ocupado ou inacessível. Por favor, tente novamente mais tarde.") 

#Função de alteração de disponibilidade do livro
def disponibilidade_livros(id):
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()

        cursor.execute("SELECT disponivel FROM livros WHERE id = ?", id)
        resultado = cursor.fetchone()

        if resultado is None:
            print("Nenhum livro encontrado")
            return
        
        estado_atual = resultado[0]
        novo_estado = "Não" if estado_atual == "Sim" else "Sim" #ternário
        cursor.execute("UPDATE livros SET disponiel = ?", (novo_estado, id)) 
        print(f"Disponibilidade do livro ID: {id} alterada para: {novo_estado}")

        conexao.commit()

    except sqlite3.OperationalError:
        print("A tabela ainda não foi criada. Cadastre livros primeiro.")
    except sqlite3.InterfaceError:
        print("O ID informado é invalido, tente novamente.")
    except Exception:
        print("Erro inexperado. Por favor, tente novamente mais tarde.")

#Função para remover livros
def remover_livros(id):
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()

        cursor.execute("DELETE FROM alunos WHERE id = ?", (id))

        if cursor.rowcount == 0:
            print(f"Nenhum livro encontrado com o ID: {id} na tabela.")
        else:
            print(f"Livro com o ID: {id} removido com sucesso.")

        conexao.commit()
    except Exception:
        print("Erro inexperado. Por favor, tente novamente mais tarde.")
    except sqlite3.InterfaceError:
        print("O ID informado é invalido, tente novamente.")
    except sqlite3.OperationalError:
        print("A tabela ainda não foi criada. Cadastre livros primeiro.")
    
    


    



    
    
