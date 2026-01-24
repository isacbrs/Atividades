import pandas as pd
import plotly.express as px
#Passo 1
tabela = pd.read_csv("cancelamentos.csv")

#Passo 2
tabela = tabela.drop(columns="CustomerID")

#Passo 3
tabela = tabela.dropna()

#Passo 4
#print(tabela["cancelou"].value_counts())
#print(tabela["cancelou"].value_counts(normalize=True)) 

#Passo 5
#criar:
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x= coluna , color="cancelou", text_autor=True)
#mostrar 
grafico.show()