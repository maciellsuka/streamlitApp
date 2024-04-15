import streamlit as st
import pandas as pd

st.header("Visualização de Dados")

if 'dados' not in st.session_state:
    st.error("Os dados não foram carregados")
else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']
    dados_filtrados = dados.head(top_n)
    st.write(dados_filtrados)
