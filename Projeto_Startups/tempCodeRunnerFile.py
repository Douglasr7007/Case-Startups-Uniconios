import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#Lendo o arquivo e trasnformando o mesmo em um dataframe 
df_startups = pd.read_csv("c:\\Users\\Dell\\OneDrive\\Desktop\\Portfolio Python\\archive (6)\\unicorns till sep 2022.csv")

#Visualiza a primeiras 5 linhas do dataframe
print(df_startups.head())

#Renomeação de colunas no local (na base de dados original) para uma melhor compreesão  
df_startups.rename(columns={
    "Company" : "Companhia",
    "Valuation ($B)" : "Avaliação Mercado ($B)",
    "Date Joined" : "Data Adesão",
    "Country" : "País",
    "City" : "Cidade",
    "Industry" : "Industria",
    "Investors" : "Investidores"
}, inplace=True)

#Substitui a str $ para vazio e altera a tipagem de object para flutuante 
df_startups["Avaliação Mercado ($B)"] = df_startups["Avaliação Mercado ($B)"].str.replace("$", "", regex=False).astype(float)


#Convertendo o tipo da data de object para datetime 
df_startups["Data Adesão"] = pd.to_datetime(df_startups["Data Adesão"])


#Verificando as observações/registros, tipagem dos dados, total de colunas e registros não nulos
df_startups.info()

#Analisando campos nulos na coluna investidores 
plt.figure( figsize=(10, 8))
plt.title("Análise de Campos Nulos")
sns.heatmap(df_startups.isnull(), cbar=False)
plt.xticks(rotation=45)  
plt.show()



#Verifa se as colunas tem valores nulos e faz a somatória dos mesmos
print(df_startups.isnull().sum())

#Verifica quantos valores tem em cada coluna
print(df_startups.nunique())


#Pegando as distribuições das industrias/startups sobre o total 
percentual_industria = df_startups["Industria"].value_counts(normalize=True)* 100

#Ordenando a distribuição dos dados em ordem decrescente 
percentual_industria_decrescente = percentual_industria.sort_values(ascending=False)

#Fazendo um filtro e pegando as 10 maiores industrias do meu conjunto de dados
percentual_industria_decrescente_top_10 = percentual_industria_decrescente.head(10)

#Reordenando como decrescente, quando faz o filtro head() ele não respeita a ordenação anterior 
percentual_industria_decrescente_top_10 = percentual_industria_decrescente_top_10.sort_values(ascending=True)

#Criando gráfico de barras
plt.figure(figsize=(10, 7))
percentual_industria_decrescente_top_10.plot( kind="barh", color="skyblue")

#Adicionando titulo e rotulos de dados 
plt.title("Top-10 Distribuição Percentual das Indústrias Startups Unicórnio", fontsize=15)
plt.xlabel("Percentual (%)", fontsize=12)
plt.ylabel("Industrias", fontsize=12)
plt.grid(axis="x", linestyle="--", alpha=0.7)

#Inserindo o percentual (%) do total como rótulo de dados através da funçao enumerate, faz a numeração por índice e valor
for i, v in enumerate(percentual_industria_decrescente_top_10):
    plt.text( v + 0.5, i, f"{v:.1f}%", va="center")

# Exibir o gráfico
plt.tight_layout()
plt.show()


#Contando o total de startups por país e extraindo o percentual dos mesmos 
percentual_paises = df_startups["País"].value_counts(normalize=True)* 100


#Adicionando titulo e rotulos de dados 
plt.figure(figsize=(10, 6))
plt.title("Top-5 Percentual de Startups Unicórnio por País", fontsize=15)
plt.pie(
    percentual_paises.head(5),
    labels=percentual_paises.index[0:5],
    shadow=True,
    startangle=90,
    autopct="%1.1f%%",
    colors=["skyblue", "lightgreen", "gold", "brown", "gray"]
);

plt.show()
print(percentual_paises.head(5))


#Criando coluna de ano e mês no dataframe 
df_startups["Mês"] = pd.DatetimeIndex(df_startups["Data Adesão"]).month
df_startups["Ano"] = pd.DatetimeIndex(df_startups["Data Adesão"]).year


# Agrupamento para manter a coluna de avaliação 
startups_por_pais = df_startups.groupby(by=["País", "Companhia", "Mês", "Ano"]).agg(
    Quantidade=("Companhia", "count"),
    Avaliação_mercado=("Avaliação Mercado ($B)", "sum")
).reset_index()


# Renomear coluna contada
startups_por_pais.rename(columns={"Companhia": "Quantidade"}, inplace=True)



#Quantidade de empresas que viraram startups no Brasil e Estados Unidos
qtd_brasil = startups_por_pais.loc[
    startups_por_pais["País"] == "Brazil", "Quantidade"
].sum()

qtd_estados_unidos = startups_por_pais.loc[
    startups_por_pais["País"] == "United States", "Quantidade"
].sum()

print(f"Brasil Tem {qtd_brasil} Startups no Total \nEstados Unidos Tem {qtd_estados_unidos} Startups no Total")


análise_por_país = startups_por_pais.groupby("País")[["Avaliação_mercado"]].sum().reset_index()
top_5 = análise_por_país[["País", "Avaliação_mercado"]].sort_values(by="Avaliação_mercado", ascending=False).head(5).reset_index()


plt.figure(figsize=(10, 6))
plt.bar(top_5["País"], top_5["Avaliação_mercado"], color='skyblue')
plt.title("Top-5 Países com Maior Avaliação de Mercado ($B) por Startups")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()


# Adiciona os rótulos no topo das barras
for i, valor in enumerate(top_5["Avaliação_mercado"]):
    plt.text(i, valor + 1, f'{valor:.0f}', ha='center', va='bottom', fontsize=10)

plt.show()