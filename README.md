# Santander 2025 - Ciência de Dados com Python - ETL com Python e Pandas

##  Descrição do Projeto
Este projeto faz parte do desafio da Santander  bootcamp da Dio 2025. O objetivo principal é demonstrar o funcionamento de um processo **ETL** (Extract, Transform, Load), que é a base da engenharia de dados. 

Originalmente, o projeto utilizava uma API externa e o GPT-4 da OpenAI para gerar mensagens personalizadas. Nesta versão, o fluxo foi adaptado
para rodar de forma local e eficiente, simulando o comportamento da IA para garantir que a lógica de transformação de dados seja concluída com sucesso.


##  Fluxo ETL

1.  **Extract (Extração):**
    * Os dados de entrada (ID e Nome) são simulados a partir de uma lista Python.
    * Utilizamos a biblioteca **Pandas** para converter esses dados em um DataFrame e manipular os IDs de forma estruturada.

2.  **Transform (Transformação):**
    * Nesta etapa, criamos uma função que simula a lógica de um especialista em marketing bancário.
    * Para cada usuário extraído, uma mensagem personalizada sobre investimentos é gerada automaticamente, enriquecendo o dado original.

3.  **Load (Carregamento):**
    * Os dados transformados são consolidados em um formato JSON.
    * O resultado final é exibido e salvo em um arquivo, simulando o carregamento em um banco de dados ou sistema de destino.

##  Tecnologias Utilizadas
* **Python 3**
* **Pandas:** Para manipulação e estruturação dos dados.
* **JSON:** Para organização e saída dos dados finais.
* **Google Colab:** Ambiente de desenvolvimento utilizado.

