# Agrupar por País e data (Ano + Mês)
startups_por_pais["Data"] = pd.to_datetime(startups_por_pais["Ano"].astype(str) + "-" + startups_por_pais["Mês"].astype(str) + "-01")

# Selecionar os principais países (por total de startups)
top_paises = startups_por_pais.groupby("País")["Quantidade"].sum().sort_values(ascending=False).head(2).index

# Filtrar só os países principais
df_top = startups_por_pais[startups_por_pais["País"].isin(top_paises)]

# Pivotar para formato ideal para gráfico
df_pivot = df_top.pivot_table(index="Data", columns="País", values="Quantidade", aggfunc="sum").fillna(0)

# Ordenar por data
df_pivot = df_pivot.sort_index()

# Plotar gráfico
plt.figure(figsize=(12, 6))
for pais in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[pais], label=pais)

plt.title("Crescimento de Startups por País ao Longo do Tempo")
plt.xlabel("Ano")
plt.ylabel("Quantidade de Startups")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
