#Importando bibliotecas
import streamlit as st
import pandas as pd

dic_df = {
    'Nome':['Mateus','Simone','Raimundo','Rosa','Mateus','Mateus','Rosa','Simone','Rosa','Raimundo'],
    'Valores':[5,6,7,1,3,8,9,4,5,6]
}

df = pd.DataFrame(dic_df['Valores'], index=dic_df['Nome'],columns=['Valores'])
df.head()

st.write("""
    # Meu Primeiro APP
    Hello *World*!
""")

st.line_chart(df)