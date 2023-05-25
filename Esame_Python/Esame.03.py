import requests
from bs4 import BeautifulSoup
import scraping
import pandas as pd 
import re
import matplotlib.pyplot as plt
import numpy as np

url = 'https://www.imdb.com/chart/top/'
dictionary_path = '.\\..\\data\\dictionary.json'
items = 250 #MAX 250
scraping = scraping.Scraping(dictionary_path, items)
movie_dict = scraping.load_dictionary(url)

#Creazione del dataframe a partire dal dizzionario 
df = pd.DataFrame(movie_dict)

#Invertire le righe con le colonne
df = df.transpose()

#Pulizia del dataframe
#Rimuovo tutti i record che non hanno i valori in dollari
df = df[df['budget'].str.contains('\$', na=True)]
df = df[df['revenue'].str.contains('\$', na=True)]

#Rimozione simboli valute nelle colonne budget e revenue
df['budget'] = df['budget'].apply(lambda x: re.sub(r'[^\d.,]+', '', x))
df['revenue'] = df['revenue'].apply(lambda x: re.sub(r'[^\d.,]+', '', x))

#Rimozione delle virgole nell colonne budget e revenue
df['budget'] = df['budget'].str.replace(',', '')
df['revenue'] = df['revenue'].str.replace(',', '')

#Cambio il tipo nelle colonne budget e revenue da str a float
df['budget'] = df['budget'].astype(float)
df['revenue'] = df['revenue'].astype(float)

df['date'] = df['date'].astype(int)

# Converti la colonna del budget in numeri
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')

# Calcola la media del budget
media_budget = df['budget'].mean()

# Filtra i valori che superano 360000000 nella colonna del budget
df.loc[df['budget'] > 360000000, 'budget'] = media_budget

#Rimosso la notazione scentiva all'interno del dataframe 
pd.set_option('display.float_format', '{:.2f}'.format)

#Controllo presenza valori nulli all'inerno del dataframe
valori_nulli_colonne = df.isnull().sum()
print(valori_nulli_colonne)
print('--------------------------------------------------------------------')

#Creo una funzione per ricavere il decennio di uscita
def get_decade(anno):
    decennio = str(anno)[-2:-1] + "0"
    return decennio

#Creo una nuova colonna che indici il decennio di uscita del film 
df['decade'] = df['date'].apply(get_decade)

#Creo una nuova colonna che indici il profitto per ogni film 
df['profit'] = (df['revenue'] - df['budget']) / df['budget'] * 100

df = df.reset_index()

#Statistica di base 
print(df.describe())
print('--------------------------------------------------------------------')

#film con budget più alto
film_budget_max = df.loc[df['budget'].idxmax()]
print("Il film con il budget più alto è:\n", film_budget_max)
print('--------------------------------------------------------------------')


#Film con profitto più alto 
film_profit_max = df.loc[df['profit'].idxmax()]
print("Il film con il profitto più alto è:\n", film_profit_max)
print('--------------------------------------------------------------------')


#Film più nuovo
film_oldest = df.loc[df['date'].idxmax()]
print("Il film più nuovo è:\n", film_oldest)
print('--------------------------------------------------------------------')

#Correlazioni
# Estrai le colonne di interesse come array NumPy
budget = df['budget'].to_numpy(dtype=np.float64)
revenue = df['revenue'].to_numpy(dtype=np.float64)

# Calcola la correlazione utilizzando np.corrcoef()
correlation = np.corrcoef(budget, revenue)[0, 1]
print(correlation)

# Creazione del grafico di dispersione
plt.scatter(budget, revenue)
plt.title("Correlazione tra Budget e Revenue")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.grid(True)

# Stampa della correlazione nel grafico
plt.text(1e10, 1e10, f"Correlazione: {correlation:.2f}", color='red')

# Mostra il grafico
plt.show()

#Grafici delle correlazioni
# Estrai le colonne di interesse come array NumPy
profit = df['profit'].to_numpy(dtype=np.float64)
budget = df['budget'].to_numpy(dtype=np.float64)

# Calcola la correlazione utilizzando np.corrcoef()
correlation = np.corrcoef(profit, budget)[0, 1]
print(correlation)
# Creazione del grafico di dispersione
plt.scatter(profit, budget)
plt.title("Correlazione tra Profit e Budget")
plt.xlabel("Profit")
plt.ylabel("Budget")
plt.grid(True)

# Stampa della correlazione nel grafico
plt.text(1e10, 1e8, f"Correlazione: {correlation:.2f}", color='red')

# Mostra il grafico
plt.show()



