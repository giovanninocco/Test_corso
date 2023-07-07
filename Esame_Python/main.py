import scraping_global_blue



def main():
    scraping = scraping_global_blue.ScrapingBlobalBlue()
    result = scraping.run_scraping(docId='12043099437770267167', purchaseAmount='259.70')
    print(result)


if __name__ == "__main__":
    main()