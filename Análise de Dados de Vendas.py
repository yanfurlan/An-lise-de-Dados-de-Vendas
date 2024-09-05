import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Leitura dos dados
df = pd.read_csv('/dados_vendas.csv')

# 2. Limpeza dos dados
df.dropna(inplace=True)  # Remove valores nulos
df['Data'] = pd.to_datetime(df['Data'])  # Converte a coluna de data para datetime

# 3. Análise Exploratória de Dados (EDA)

# Estatísticas descritivas
print("Estatísticas Descritivas:")
print(df.describe())

# Receita total por produto
receita_produto = df.groupby('Produto')['Receita'].sum().reset_index()
print("\nReceita Total por Produto:")
print(receita_produto)

# Receita total por região
receita_regiao = df.groupby('Região')['Receita'].sum().reset_index()
print("\nReceita Total por Região:")
print(receita_regiao)

# 4. Visualização de Dados

# Gráfico de Barras: Receita por Produto
plt.figure(figsize=(10,6))
sns.barplot(x='Produto', y='Receita', data=receita_produto, palette='viridis')
plt.title('Receita por Produto')
plt.xlabel('Produto')
plt.ylabel('Receita Total')
plt.show()

# Gráfico de Barras: Receita por Região
plt.figure(figsize=(10,6))
sns.barplot(x='Região', y='Receita', data=receita_regiao, palette='magma')
plt.title('Receita por Região')
plt.xlabel('Região')
plt.ylabel('Receita Total')
plt.show()

# Gráfico de Linha: Evolução da Receita ao longo do tempo
plt.figure(figsize=(10,6))
df.groupby('Data')['Receita'].sum().plot(marker='o')
plt.title('Evolução da Receita ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Receita Total')
plt.grid(True)
plt.show()

# Gráfico de Heatmap: Correlação entre variáveis
# Remover colunas não numéricas antes de calcular a correlação
df_numerico = df.select_dtypes(include=[float, int])
plt.figure(figsize=(8,6))
sns.heatmap(df_numerico.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()
