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

#Criando um agrupamento por país, e somando a avaliação de mercado dos mesmo.
#Extraindo os top-5 países da variável, organizando os valores em ordem decrescente, chamando os 5 primeiros países e resetando o índice
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