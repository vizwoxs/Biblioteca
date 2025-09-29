import funcao as fun
import streamlit as st

st.set_page_config(page_title="Biblioteca SENAI", layout="centered")
st.title("Biblioteca SENAI")
menu = st.sidebar("Menu", ["Cadastrar Livro", "Listar Livros", "Atualizar Disponibilidade", "Remover Livro"])