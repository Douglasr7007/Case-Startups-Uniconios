

percentual_paises = df_startups["País"].value_counts(normalize=True)* 100


#Adicionando titulo e rotulos de dados 
plt.figure(figsize=(15, 6))
plt.title("Percentual de Startups Unicórnio por País", fontsize=15)
plt.pie(
    percentual_paises.head(4),
    labels=percentual_paises.index[0:4],
    shadow=True,
    startangle=90,
    autopct="%1.1f%%",
    colors=["skyblue", "lightgreen", "gold", "brown"]
);

plt.show()