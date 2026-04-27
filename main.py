import pandas as pd
from funcoes import funcao_filto
import streamlit as st
idade = st.slider('Selecione a idade:', 0, 100, 25)

data1 = st.date_input('Digite a data inicial:')
data2 = st.date_input('Digite a data final:')

if st.button('Buscar'):
    if data1 and data2:
        if data1 > data2:
            st.write("A data inicial deve ser menor que a final!")
        else:
            tabela = funcao_filto(idade,data1,data2)
            tabela_pd = pd.DataFrame(tabela, columns=['nome_cliente','idade'])
            st.dataframe(tabela_pd)
    else:
        st.write("Selecione as duas datas!")
