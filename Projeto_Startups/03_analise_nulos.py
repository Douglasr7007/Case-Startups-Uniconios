
#Analisando campos nulos na coluna investidores 
plt.figure( figsize=(6, 8))
plt.title("Análise de Campos Nulos")
sns.heatmap(df_startups.isnull(), cbar=False)
plt.xticks(rotation=45)  
plt.show()



#Verifa se as colunas tem valores nulos e faz a somatória dos mesmos
print(df_startups.isnull().sum())

#Verifica quantos valores tem em cada coluna
print(df_startups.nunique())
