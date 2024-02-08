# importando frameworks
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib as mpl 
# melhorar a visualização %matplotlib inline mpl.style.use('ggplot') plt.style.use('fivethirtyeight') sns.set(context='notebook', palette='dark', color_codes=True) 
import matplotlib.patches as mpatches


#leitura da tabela cvs com a biblioteca pandas 
dados_musicas = pd.read_csv('https://raw.githubusercontent.com/letpires/7DaysOfCodeSpotifyML/main/dataset.csv', index_col=0) 
dados_musicas.head()


# Extraindo a descrição dos atributos numéricos 
dados_musicas.describe()
# visualizando suas dimensões 
dados_musicas.shape
# visualizando a quantidade em cada linha e seu formato 
dados_musicas.info()

# Artistas únicos e contagem de músicas por artista 
print(dados_musicas['artists'].unique().shape) 
print(dados_musicas['artists'].value_counts())


# ordenar em ordem decrescente as variáveis por seus valores ausentes 
(dados_musicas.isnull().sum() / dados_musicas.shape[0]).sort_values(ascending=False)

dados_musicas.isnull().sum()

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
            
missing_visualization(dados_musicas)

#As 100 músicas mais populares versus todo o conjunto de dados 
sorted_df = dados_musicas.sort_values('popularity', ascending = False).head(100) 
sorted_df.head()
dados_musicas.isna().sum() #check for null values
dados_musicas.isna().sum() #check for null values

dados_musicas.shape
dados_musicas.columns

dados_musicas.duration_ms

dados_musicas["duration_ms"]= dados_musicas["duration_ms"].replace("durations_ms", ) # 
dados_musicas

artistas_popularidade = dados_musicas[['artists', 'popularity']] 
artistas_populares = artistas_popularidade.groupby("artists").mean().sort_values(by='popularity', ascending=False).reset_index() 

#Trazendo somente os 5 primeiros 
artistas_populares = artistas_populares.head() 
artistas_populares

# Buscar entender melhor os outliers!
artistas_populares.plot.barh(color="hotpink") 
##visualize the data 
plt.title("TOP 5 Most Popular Artists") 
plt.show()

# #Top 5 artistas populares 
popular_artists = dados_musicas.groupby("artists").count().sort_values(by='popularity', ascending=False)['popularity'][:5] 
popular_artists
#top 5 longest songs or tracks 
long_songs = dados_musicas[["track_name", "duration_ms"]].sort_values(by="duration_ms", ascending=False)[:5] 
long_songs

sns.barplot(x="duration_ms", y="track_name", data= long_songs, color = 'hotpink') 
plt.title("Top 5 Longest songs") 
plt.show()

#Top 5 most trending genre 
trend_genre = dados_musicas[["track_genre", "popularity"]].sort_values(by="popularity", ascending=False)[:5] 
trend_genre

sns.barplot(x="track_genre",y="popularity", data=trend_genre, color = 'hotpink') 
plt.title("Top trending genre") 
plt.show()

#Top 5 most danceable songs 
danceable = dados_musicas[["track_name", "artists", "danceability"]].sort_values(by="danceability", ascending=False)[:5] 
danceable

#add colors 
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#ffb6c1'] 
plt.pie(x="danceability", data=danceable, autopct='%1.2f%%', labels=danceable.track_name, colors = colors) 
plt.title("Top 5 Most Danceable Songs") 
plt.show()

#Encontrando correlação entre as variáveis 
dados_musicas.describe()

corr_table = dados_musicas.corr(method="pearson") #get variables the correlation
corr_table


#Plotando a tabela de correlação usando o Seaborn. 
plt.figure(figsize=(16,4)) 
sns.heatmap(corr_table, annot=True, fmt=".1g") 
plt.title("Correlation Heatmap between variables") 
plt.show() #mostrando o plot
