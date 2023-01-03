#Importando bibliotecas
import streamlit as st
import pandas as pd

dic_df = {
    'Nome':['Mateus','Simone','Raimundo','Rosa','Mateus','Mateus','Rosa','Simone','Rosa','Raimundo'],
    'Valores':[5,6,7,1,3,8,9,4,5,6]
}

df = pd.DataFrame(dic_df)

st.write("""
    # Meu Primeiro APP
    Hello *World*!
""")

st.line_chart(df.groupby('Nome').sum())

number = st.slider('Escolha um número', 0, 100)

if number%2==0:
    st.write('O múmero é par.')
else:
    st.write('O número é ímpar.')

arquivo = st.file_uploader("Escolha um arquivo de texto")
pet = st.radio('Escolhar um animal',['Gato','Cachorro','Papagaio','Cavalo'])

