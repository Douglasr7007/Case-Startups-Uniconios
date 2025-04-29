
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
