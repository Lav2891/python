from __future__ import print_function
from bs4 import BeautifulSoup
import requests
result = requests.get("https://www.moneycontrol.com/india/stockpricequote/A")

c = result.content

soup = BeautifulSoup(c)
print(soup)

mydivs = soup.findAll("meta", {"http-equiv": "Content-Type"})
print(mydivs)