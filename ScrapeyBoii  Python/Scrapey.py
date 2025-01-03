from bs4 import BeautifulSoup
import requests
import time
import random

no_of_pages = 5
titles = []


def get_urls():
    page_urls = []
    for page in range(1, no_of_pages):
        url = 'https://www.ebay.co.uk/sch/i.html?_dmd=2&icon' \
              'V2Request=true&_ssn=the_gently_mad&store_cat=' \
              '0&store_name=thegentlymad&_oac=4&_pgn=' + str(page)
        page_urls.append(url)
    return page_urls


def extract(url):
    titles = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    for title in soup.find_all('h3'):
        if 'title' in str(title):
            print(title)
            titles.append(title)
    return titles


def scrapey():
    #time.sleep(random.randint(2, 7))
    print('working...')
    for page in urls:
        print(page)
        titles.append(extract(page))
        print(titles)
    return titles


urls = get_urls()
titles = scrapey()

print(titles)

