import requests
from bs4 import BeautifulSoup
from datetime import datetime
import schedule
import time


def track_book_price():
    print(datetime.now())
    # pageCount is number of pages that you want to scrape
    pageCount = 4
    for i in range(1, pageCount):
        url = f'https://books.toscrape.com/catalogue/page-{2}.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # There are different flavours for soup. like find to find 1 element, findAll to get all elements
        # or select to specify css selector and get all elements
        list_items = soup.findAll('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        # Get info by looping through items
        for i in list_items:
            # print(i.find('h3').a["title"])
            print(i.find("img")['alt'])
            print(i.find('p', class_='price_color').text)
            print(i.findNext('p', class_='instock availability').text.strip())
            print('===================')

track_book_price()
schedule.every(1).minutes.do(track_book_price)

while True:
    schedule.run_pending()
    time.sleep(1)
