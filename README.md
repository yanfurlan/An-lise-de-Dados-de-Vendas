Análise de Dados de Vendas

Este projeto realiza uma análise exploratória de dados de vendas utilizando Python, com as bibliotecas Pandas para manipulação de dados, Matplotlib e Seaborn para visualização.
Requisitos

Antes de executar o código, certifique-se de ter as seguintes bibliotecas Python instaladas:

    pandas
    matplotlib
    seaborn

Você pode instalar essas bibliotecas utilizando o pip:

bash

pip install pandas matplotlib seaborn

Arquivo CSV

Certifique-se de ter o arquivo dados_vendas.csv. O arquivo deve conter, no mínimo, as seguintes colunas:

    Data: A data da venda
    Produto: O nome do produto vendido
    Receita: O valor da receita gerada pela venda
    Região: A região onde a venda foi realizada

Código

O código realiza as seguintes etapas:

    Leitura dos Dados: Carrega os dados do arquivo CSV.
    Limpeza dos Dados: Remove valores nulos e converte a coluna de data para o formato datetime.
    Análise Exploratória de Dados (EDA):
        Exibe estatísticas descritivas.
        Calcula e exibe a receita total por produto.
        Calcula e exibe a receita total por região.
    Visualização de Dados:
        Gráfico de Barras: Receita total por produto.
        Gráfico de Barras: Receita total por região.
        Gráfico de Linha: Evolução da receita ao longo do tempo.
        Gráfico de Heatmap: Correlação entre variáveis.

Executando o Código

Para executar o código, salve-o em um arquivo Python, por exemplo, analise_vendas.py, e execute-o com Python:

bash

python analise_vendas.py

Exemplo de Saída

O código gera os seguintes gráficos:

    Gráfico de barras mostrando a receita total por produto.
    Gráfico de barras mostrando a receita total por região.
    Gráfico de linha mostrando a evolução da receita ao longo do tempo.
    Heatmap mostrando a correlação entre variáveis.