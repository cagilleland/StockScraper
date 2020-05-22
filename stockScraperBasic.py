#Stock  Scraper Basic

import requests
from bs4 import BeautifulSoup

requested_symbol=input("What stock would you like me to check? ")
URL = 'https://finance.yahoo.com/quote/'+requested_symbol
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
current_price = soup.find("span",{"data-reactid":"14"})
after_price = soup.find("span" , class_="C(black) Fz(14px) Fw(500)")

print(current_price.prettify())
print(after_price.prettify())

print(current_price.text)
print(after_price.text)
