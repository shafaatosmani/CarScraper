from bs4 import BeautifulSoup
import requests

url = 'https://www.carfax.com/Used-BMW-M4_w51'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)
