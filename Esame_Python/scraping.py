import os 
import json 
import requests
from bs4 import BeautifulSoup

class Scraping:
    def  __init__(self) -> None:
        
        passimport os 
import json 
import requests
from bs4 import BeautifulSoup

class Scraping:
    def  __init__(self, dictionary_path, items=-1) -> None:
        self.dictionary_path = dictionary_path
        self.items = items

    def load_dictionary(self, root_url):
        if os.path.exists(self.dictionary_path):
            
            # Apri il file in modalità lettura
            with open(self.dictionary_path, "r") as file:
            # Leggi il contenuto del file JSON
                return json.load(file)
            
        contenuto_file = self.run_scraping(root_url)
        with open(self.dictionary_path, "w") as file:
            # Serializza il dizionario in formato JSON e scrivi sul file
            json.dump(contenuto_file, file)
#        dizionario = json.loads(file_path)
            

    def run_scraping(self, root_url):
        title_list = []
        date_list = []
        rating_list = []
        budget_list =[]
        revenue_list = [] 
        ranking_list = [] 

        movie_dict = {}

        response = requests.get(root_url)

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

        else:
            print('Errore nella richiesta GET:', response.status_code)



        # Effettua la richiesta GET alla pagina web con un'intestazione User-Agent personalizzata

        for _, elemento in enumerate(movie_links):
            if _ > self.items:
                break
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
                title = ''
                if title_tmp != None:
                    title = title_tmp.contents[0].text

                # Estrai il budget del film
                budget_tmp = soup.select_one('[data-testid="title-boxoffice-budget"]')
                budget = '0'
                if budget_tmp != None:
                    budget = budget_tmp.contents[1].text
                    budget = budget.split(' ')[0]

                # Estrai i ricavi del film 
                revenue_tmp = soup.select_one('[data-testid="title-boxoffice-cumulativeworldwidegross"]') 
                revenue = '0'
                if revenue_tmp != None:
                    revenue = revenue_tmp.contents[1].text

                # Estrai la data di uscita del film
                date_tmp = soup.select_one('[data-testid="title-boxoffice-openingweekenddomestic"]')
                date = '0'
                if date_tmp != None:
                    date = date_tmp.contents[1].text
                    date = date.split(', ')[-1]

                # Estrai il rating del film
                rating_temp = soup.select_one('[data-testid="hero-rating-bar__aggregate-rating__score"]')
                rating = '0'
                if rating_temp != None:
                    rating = rating_temp.contents[0].text

                title_list.append(title)
                date_list.append(date)
                rating_list.append(rating)
                ranking_list.append(_+1)
                budget_list.append(budget)
                revenue_list.append(revenue)

            else:
                print("Errore nella richiesta HTTP:", response.status_code)  

        for i in range(len(title_list)):
            movie_dict[title_list[i]] = {
                "date": date_list[i],
                "rating": rating_list[i],
                "budget": budget_list[i],
                "revenue": revenue_list[i],
                "ranking": ranking_list[i]
            }     

        return movie_dict
    



    def load_dictionary(self, root_url):
        file_path = 'data/dictionary.json'
        if os.path.exists(file_path):
            
            # Apri il file in modalità lettura
            with open(file_path, "r") as file:
            # Leggi il contenuto del file JSON
                contenuto_file = file.read()
                return contenuto_file
            
        contenuto_file = self.run_scraping(root_url)
        with open(file_path, "w") as file:
            # Serializza il dizionario in formato JSON e scrivi sul file
            json.dump(contenuto_file, file)
#        dizionario = json.loads(file_path)
            

    def run_scraping(self, root_url):
        title_list = []
        date_list = []
        rating_list = []
        budget_list =[]
        revenue_list = [] 
        ranking_list = [] 

        movie_dict = {}

        response = requests.get(root_url)



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

            else:
                print("Errore nella richiesta HTTP:", response.status_code)  

        for i in range(len(title_list)):
            movie_dict[title_list[i]] = {
                "date": date_list[i],
                "rating": rating_list[i],
                "budget": budget_list[i],
                "revenue": revenue_list[i],
                "ranking": ranking_list[i]
            }     

        return movie_dict
