import pandas as pd

df = pd.read_csv("validacao.csv", encoding="utf-8", sep=";")

# print(df.head(10))
# Verifica a quantidade de linhas
# print(df.shape)
# print( df )
# dados = df[['Empresa', 'Nome']].head

# print(dados)
# selecionando algumas colunas

# trabalhando com loc, ele trabalha como vetor, podendo ser dimensional
# sempre seleciona as linhas primeiro
# pode ser criado selecionando as linhas que voce quer, com dois arrays [[]]
# valores = df.loc[0:3]


# trabalhando com iloc, somente dados numericos.
# valores = df.iloc[0:3]
valores = df.sort_values('Nome').head(10)

print( valores )


