import streamlit as st
import plotly.express as px

st.header("Maiores Valores")

if 'dados' not in st.session_state:
    st.error("Os dados não foram carregados")
else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']

    col1, col2, col3 = st.columns(3)

    with col1:
        mEmpenho = dados.nlargest(top_n, 'VALOREMPENHO')
        fig = px.bar(mEmpenho, x='MUNICIPIO', y='VALOREMPENHO', title='Maiores Empenhos')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        mPIBs = dados.nlargest(top_n, 'PIB')
        fig2 = px.pie(mPIBs, values='PIB', names='MUNICIPIO', title='Maiores PIBs')
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        mProp = dados.nlargest(top_n, 'PROPORCAO')
        fig3 = px.bar(mProp, x='MUNICIPIO', y='PROPORCAO', title='Maiores Gastos em Proporção ao PIB')
        st.plotly_chart(fig3, use_container_width=True)