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


![image](https://github.com/user-attachments/assets/8c8bc9bf-55c8-4d8e-85f6-588e57ef0860)



🔹 Heatmap de Valores Nulos
Através de um heatmap, identificou-se a presença de 18 registros nulos concentrados na coluna Investidores. Por sua baixa representatividade no total, foi decidido manter os registros sem prejuízo à integridade da análise.


![image](https://github.com/user-attachments/assets/97262567-7a9b-43ad-8dad-36c8f8e2ff00)




🔹 Top-10 Indústrias de Startups Unicórnio
Um gráfico de barras horizontais evidenciou as 10 indústrias mais recorrentes entre as startups unicórnio:

Fintech, Internet Software & Services e E-commerce lideram o mercado, somando quase 50% do total global.

📌 Insight Estratégico:

Empresas que almejam se tornar unicórnios devem observar atentamente esses setores, que demonstram alto potencial de crescimento e validação global. São ramos altamente promissores para novos investimentos e inovação tecnológica.

![image](https://github.com/user-attachments/assets/89dac80e-2d0e-4d23-b228-7c26e7a4c7dd)





🔹 Distribuição Global por País (Gráfico de Pizza)
A análise da distribuição geográfica revelou que:

🇺🇸 Estados Unidos concentram 66,6% das startups unicórnio do mundo.

🇨🇳 China aparece em segundo lugar com 18,2%.

📌 Insight Estratégico:

A diferença de quase 50 pontos percentuais entre EUA e China pode estar relacionada a diversos fatores: volume de investimento, ambiente regulatório, capital humano, tecnologia e ecossistema de inovação. Os Estados Unidos se destacam como o epicentro global de startups de alto valor.

![image](https://github.com/user-attachments/assets/cd0426b4-77b1-4e5c-ad3b-6706d305a4e8)





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

📝 Como Usar o Código com o Arquivo de Dados

Este projeto utiliza o arquivo unicorns 2022.csv, que contém informações sobre startups unicórnio até setembro de 2022. Para rodar o código e analisar os dados, siga as etapas abaixo:

1. Baixar ou Obter os Dados
O arquivo unicorns 2022.csv já está disponível na pasta Dados/ do repositório.

Certifique-se de que o arquivo esteja na mesma estrutura de pastas, ou seja, dentro da pasta Dados/.

2. Rodando o Código
Para rodar o código, siga os passos abaixo:

Clone o Repositório
Se ainda não fez isso, clone o repositório para o seu ambiente local usando o seguinte comando:

- git clone https://github.com/Douglasr7007/Case-Startups-Uniconios.git
- cd Case-Startups-Uniconios

Instalar Dependências
O código utiliza algumas bibliotecas que precisam ser instaladas. Para instalá-las, crie um ambiente virtual e execute o comando abaixo para instalar as dependências:

- python -m venv venv
- source venv/bin/activate  # Para sistemas Unix/Linux/MacOS
- venv\Scripts\activate     # Para Windows
- pip install -r requirements.txt

Observação: O arquivo requirements.txt deve conter as bibliotecas necessárias, como pandas, matplotlib, seaborn, entre outras.

Executar o Script

Após instalar as dependências, execute o script Case_Startups_Unicórnio.py para carregar e analisar os dados. O script faz o seguinte:

- Lê o arquivo unicorns 2022.csv na pasta Dados/.

- Realiza o tratamento e limpeza dos dados.

- Gera visualizações e análises exploratórias.

- Apresenta insights úteis sobre as startups unicórnio.

- Para rodar o script, basta usar o comando:

- python Projeto_Startups/Case_Startups_Unicórnio.py

3. Visualizações Geradas
Ao rodar o código, você verá diversos gráficos e visualizações sendo gerados, como:

- Gráfico de barras para as indústrias mais comuns entre as startups unicórnio.

- Gráfico de pizza mostrando a distribuição geográfica por país.

- Gráficos de avaliação de mercado por país.

Esses gráficos ajudarão a entender melhor os padrões de crescimento e as áreas de destaque entre as startups unicórnio até setembro de 2022.
