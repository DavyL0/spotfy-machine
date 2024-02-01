#imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import seaborn as sns

#melhor visual 
mpl.style.use('ggplot')
plt.style.use('fivethirtyeight')
sns.set(context='notebook', palette='dark', color_codes=True)

#leitura csv
df = pd.read_csv('/Users/davylopes/Documents/code/portfolio/portifolio/machinelearn/dataset 2.csv')
df.head()
df.info() 

#descreve as informaçoes do Banco.
df.shape
df.describe()

#quantidade de artistas 
print(df['artists'].unique().shape)
print(df['artists'].value_counts)
#pre-processamento de dados 
##definindo que a baixo de 70 não é importante 
#df.drop(df[df.popularity < 70].index, inplace=True)
df.isnull().sum()

#função que gera uma gráfico de barras com colunas e frequência dos dados faltantes.
def missing_visualization(df):
  quant_isnull = df.isnull().sum()
  columns = df.columns
  dic = {"colunas":[],"quant_isnull":[]}
  for coluna,quant in zip(columns,quant_isnull):
    if quant > 0:
      dic["colunas"].append(quant)
      dic["quant_isnull"].append(coluna)
  df = pd.DataFrame(dic)
  plt.figure(figsize=(15,5))
  sns.barplot(x=df["quant_isnull"],y=df["colunas"],data=df, palette="rocket")
  plt.xticks(rotation=45)
#sns.boxplot(df['duration_ms'])
##Mostra hideograma dos dados
#plt.hist(x = df['duration_ms'])


