import requests
from bs4 import BeautifulSoup
import scraping

url = 'https://www.imdb.com/chart/top/'
scraping = scraping.Scraping()
scraping.load_dictionary(url)
'''
title_list = []
date_list = []
rating_list = []
budget_list =[]
revenue_list = [] 
ranking_list = [] 

movie_dict = {}
 
# Effettua la richiesta GET alla pagina
response = requests.get(url)

# Verifica lo stato della risposta
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_links = []

    # Trova tutti gli elementi <td> con la classe "titleColumn"
    movie_cells = soup.find_all('td', class_='titleColumn')

    # Estrai il link di ciascun film
    for cell in movie_cells:
        link = cell.a['href']
        movie_links.append('https://www.imdb.com' + link)

    # Stampa la lista dei link dei film
    #for link in movie_links:
    #    print(link)

else:
    print('Errore nella richiesta GET:', response.status_code)



# Effettua la richiesta GET alla pagina web con un'intestazione User-Agent personalizzata

for _, elemento in enumerate(movie_links):
    link = elemento if _ < len(movie_links) else None

    url = link
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Controlla se la richiesta è andata a buon fine
    if response.status_code == 200:
        # Parsing del contenuto della pagina con BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Estrai il titolo del film
        title_tmp = soup.select_one('[data-testid="hero__pageTitle"]')
        if title_tmp != None:
            title = title_tmp.contents[0].text

        # Estrai il budget del film
        budget_tmp = soup.select_one('[data-testid="title-boxoffice-budget"]')
        if budget_tmp != None:
            budget = budget_tmp.contents[1].text
            budget = budget.split(' ')[0]

        # Estrai i ricavi del film 
        revenue_tmp = soup.select_one('[data-testid="title-boxoffice-cumulativeworldwidegross"]') 
        if revenue_tmp != None:
            revenue = revenue_tmp.contents[1].text

        # Estrai la data di uscita del film
        date_tmp = soup.select_one('[data-testid="title-boxoffice-openingweekenddomestic"]')
        if date_tmp != None:
            date = date_tmp.contents[1].text
            date = date.split(', ')[-1]

        # Estrai il rating del film
        rating_temp = soup.select_one('[data-testid="hero-rating-bar__aggregate-rating__score"]')
        if rating_temp != None:
            rating = rating_temp.contents[0].text

        title_list.append(title)
        date_list.append(date)
        rating_list.append(rating)
        ranking_list.append(_+1)
        budget_list.append(budget)
        revenue_list.append(revenue)

        # Stampa le informazioni del film
#        print("Title:", title)
#        print("Release date:", date)
#        print("Rating:", rating)
#        print("Ranking:", _+1)
#        print("Budget:", budget)
#        print("Revenu:", revenue)
#        print("-------------------------------------------------------------------------")
    else:
        print("Errore nella richiesta HTTP:", response.status_code)

#print("Title:", title_list)
#print("Release date:", date_list)
#print("Rating:", rating_list)
#print("Ranking:", ranking_list)
#print("Budget:", budget_list)
#print("Revenue:", revenue_list)
#print("-------------------------------------------------------------------------")


for i in range(len(title_list)):
    movie_dict[title_list[i]] = {
        "date": date_list[i],
        "rating": rating_list[i],
        "budget": budget_list[i],
        "revenue": revenue_list[i],
        "ranking": ranking_list[i]
    }

print(movie_dict)'''
