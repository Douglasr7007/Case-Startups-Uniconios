📊 Análise de Startups Unicórnio (até setembro de 2022)

Este projeto tem como objetivo explorar, tratar e analisar um conjunto de dados com informações de startups que alcançaram o status de unicórnio (avaliação de mercado igual ou superior a 1 bilhão de dólares), até setembro de 2022. Através de gráficos, agregações e visualizações, foram gerados insights estratégicos sobre setores promissores, distribuição geográfica e potencial de mercado.

📁 Estrutura do Projeto

1° Importação & Leitura dos Dados (ETL)

- Bibliotecas utilizadas: Pandas, NumPy, Matplotlib, Seaborn

- Leitura do arquivo CSV e criação do DataFrame

2° Tratamento e Limpeza de Dados

- Renomeação de colunas para melhor legibilidade

- Conversão da coluna de avaliação de mercado para tipo float

- Conversão da data de adesão para o tipo datetime

- Verificação de tipos de dados e dados ausentes

3° Análise Exploratória e Geração de Insights

- Gráficos de distribuição por indústria e país

- Agregações por ano, mês e avaliação total por região

- Geração de insights estratégicos para investidores e empreendedores


📈 Principais Análises e Insights


🔹 Heatmap de Valores Nulos
Através de um heatmap, identificou-se a presença de 18 registros nulos concentrados na coluna Investidores. Por sua baixa representatividade no total, foi decidido manter os registros sem prejuízo à integridade da análise.

🔹 Top-10 Indústrias de Startups Unicórnio
Um gráfico de barras horizontais evidenciou as 10 indústrias mais recorrentes entre as startups unicórnio:

Fintech, Internet Software & Services e E-commerce lideram o mercado, somando quase 50% do total global.

📌 Insight Estratégico:

Empresas que almejam se tornar unicórnios devem observar atentamente esses setores, que demonstram alto potencial de crescimento e validação global. São ramos altamente promissores para novos investimentos e inovação tecnológica.

🔹 Distribuição Global por País (Gráfico de Pizza)
A análise da distribuição geográfica revelou que:

🇺🇸 Estados Unidos concentram 66,6% das startups unicórnio do mundo.

🇨🇳 China aparece em segundo lugar com 18,2%.

📌 Insight Estratégico:

A diferença de quase 50 pontos percentuais entre EUA e China pode estar relacionada a diversos fatores: volume de investimento, ambiente regulatório, capital humano, tecnologia e ecossistema de inovação. Os Estados Unidos se destacam como o epicentro global de startups de alto valor.

🔹 Avaliação de Mercado por País (Gráfico de Barras)
O ranking de avaliação de mercado em bilhões de dólares por país mostrou:

País	               Avaliação de Mercado ($B)
🇺🇸 Estados Unidos           	2.070
🇨🇳 China                     	 679

📌 Insight Estratégico:

A diferença de mais de 1.390 bilhões de dólares entre EUA e China consolida os Estados Unidos como a potência máxima na criação e valorização de startups. Dentre os setores, o Fintech foi o maior responsável por esse destaque.

📅 Variáveis Criadas
Para análise temporal:

Ano e Mês foram extraídos da data de adesão, permitindo agrupamentos por período para futuras análises sazonais.

💡 Conclusão Geral
Este projeto demonstrou como é possível, com uso de Python e bibliotecas de análise de dados, extrair informações valiosas e aplicáveis ao mundo real. Através de uma análise bem estruturada, foram gerados insights que podem apoiar empreendedores, investidores e pesquisadores na tomada de decisão sobre onde e como investir.

🛠️ Tecnologias Utilizadas
- Python 3.11

- Pandas

- NumPy

- Matplotlib

- Seaborn

- VS Code

🧠 Habilidades Demonstradas
Manipulação e limpeza de dados

Análise exploratória e visualização

Extração de insights de negócios

Criação de gráficos impactantes

Comunicação de resultados

📌 Autor == Douglas Ribeiro da Silva 

• LinkedIn == https://www.linkedin.com/in/douglas-ribeiro-da-silva/

• GitHub == https://github.com/Douglasr7007/

