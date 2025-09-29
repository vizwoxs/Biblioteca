import funcao as fun
import streamlit as st

st.set_page_config(page_title="Biblioteca SENAI", layout="centered")
st.title("Biblioteca SENAI")
menu = st.sidebar.radio("Menu", ["Sobre", "Cadastrar Livro", "Listar Livros", "Atualizar Disponibilidade", "Remover Livro"])

#Cadastrar livro
if menu == "Cadastrar Livro":
    st.subheader("Cadastrar novo livro")
    titulo = st.text_input("Titulo do Livro")
    autor = st.text_input("Autor do livro")
    ano = st.text_input("Ano de lançamento do livro")

    if st.button("Cadastrar"):
        st.success("Livro cadastrado com sucesso")
        if titulo and autor:
            mensagem = fun.inserir_dados(titulo, autor, ano)
        else:
            st.warning("Preencha todos os campos")