
#Pegando as distribuições das industrias/startups sobre o total 
percentual_industria = df_startups["Industria"].value_counts(normalize=True)* 100

#Ordenando a distribuição dos dados em ordem decrescente 
percentual_industria_decrescente = percentual_industria.sort_values(ascending=False)

#Fazendo um filtro e pegando as 10 maiores industrias do meu conjunto de dados
percentual_industria_decrescente_top_10 = percentual_industria_decrescente.head(10)

#Reordenando como decrescente, quando faz o filtro head() ele não respeita a ordenação anterior 
percentual_industria_decrescente_top_10 = percentual_industria_decrescente_top_10.sort_values(ascending=True)

#Criando gráfico de barras
plt.figure(figsize=(12, 7))
percentual_industria_decrescente_top_10.plot( kind="barh", color="skyblue")

#Adicionando titulo e rotulos de dados 
plt.title("Distribuição Percentual das Indústrias Startups Unicórnio", fontsize=15)
plt.xlabel("Percentual (%)", fontsize=12)
plt.ylabel("Industrias", fontsize=12)
plt.grid(axis="x", linestyle="--", alpha=0.7)

#Inserindo o percentual (%) do total como rótulo de dados através da funçao enumerate, faz a numeração por índice e valor
for i, v in enumerate(percentual_industria_decrescente_top_10):
    plt.text( v + 0.5, i, f"{v:.1f}%", va="center")

# Exibir o gráfico
plt.tight_layout()
plt.show()
