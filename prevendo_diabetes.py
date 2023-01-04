#Importando bibliotecas
import streamlit as st
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#Importando o DataFrame
df = pd.read_csv('diabetes.csv')
df.head()

#Separando em alvo e variáveis
x = df.drop(columns=['Outcome'])
y = df['Outcome']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

tree_clf = DecisionTreeClassifier(criterion='entropy',max_depth=3)
tree_clf.fit(x_train, y_train) 

#Criando o app em streamlit
#Título
st.write("# Prevendo Diabetes")
#Cabeçalho
st.subheader("Informações dos dados")
#Nome do usuário
user=st.sidebar.text_input("Escreva seu Nome: ")

#Escrevendo o nome do usuário
st.write("Paciente:", user)

#Definindo função para solicitar dados e criar dataframe
def get_user_date():
    gravidez = st.sidebar.slider('Gravidez', 0,15,1,step=1)
    glicose = st.sidebar.slider('Glicose',0,200,110)
    pressao = st.sidebar.slider('Pressão Sanguínea',0,122,72)
    pele = st.sidebar.slider('Espessura da Pele',0,99,20)
    insulina = st.sidebar.slider('Insulina',0,900,30)
    imc = st.sidebar.slider('IMC',0.0,70.0,15.0)
    hfd = st.sidebar.slider('Histórico Familiar de Diabetes',0.0,3.0,.0)
    idade = st.sidebar.slider('Idade',15,100,21)
    #Dicionário para receber informações
    user_dic = {
        'Gravidez':gravidez,
        'Glicose':glicose,
        'Pressão':pressao,
        'Pele':pele,
        'Insulina':insulina,
        'IMC': imc,
        'HFD': hfd,
        'Idade': idade
    }
    variaveis= pd.DataFrame(user_dic)
    return variaveis

variaveis_do_usuario = get_user_date()

#Criando Gráfico

graf = st.bar_chart(variaveis_do_usuario)

#Previsão do resultado

previsao = tree_clf.predict(variaveis_do_usuario)
st.subheader('Previsões')
st.write(previsao)

