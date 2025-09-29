import streamlit as st
import funcao as fun


fun.tabela()

st.set_page_config(page_title="Biblioteca SENAI", layout="centered")
st.title("Biblioteca SENAI")

menu = st.sidebar.radio("Menu", ["Sobre", "Cadastrar Livro", "Listar Livros", "Atualizar Disponibilidade", "Remover Livro"])

#Informações do sistema
if menu == "Sobre":
    st.markdown("""
    ### Bem-vindo à Biblioteca SENAI!
    Este sistema permite cadastrar, listar, atualizar e remover livros de forma simples e rápida.
    Use o menu à esquerda para navegar pelas funcionalidades.
    """)

#Cadastrar livro
elif menu == "Cadastrar Livro":
    st.subheader("Cadastrar novo livro")
    titulo = st.text_input("Título do Livro")
    autor = st.text_input("Autor do Livro")
    ano = st.number_input("Ano de lançamento", min_value=0, max_value=2100, step=1)

    if st.button("Cadastrar"):
        if titulo and autor:
            mensagem = fun.inserir_dados(titulo, autor, ano)
            st.success(mensagem)
        else:
            st.warning("Preencha todos os campos.")

#Tabela de livro
elif menu == "Listar Livros":
    st.subheader("Livros cadastrados")
    livros = fun.listar_livros()

    if livros:
        st.table(livros)
    else:
        st.info("Nenhuma tabela criada")

#Atualização
elif menu == "Atualizar Disponibilidade":
    st.subheader("Disponibilidade do Livro")
    disponivel = st.text_input("Titulo do livro")

    fun.disponibilidade_livros(disponivel)

    if st.button("Atualizar"):
        resultado = fun.disponibilidade_livros(disponivel)
        st.success(resultado)
    else:
        st.warning("Informe o título do livro.")

#remover livro
elif menu == ("Remover Livro"):
    st.subheader("Eliminação de livros já existentes no sistema")
    titulo = st.text_input("Digite o título do livro que deseja remover")
    if st.button("Remover"):
        if titulo:
            resultado = fun.remover_livros(titulo)
            st.success(resultado)
        else:
            st.warning("Informe o título do livro.")






