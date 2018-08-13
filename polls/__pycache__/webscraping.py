from __future__ import print_function
from bs4 import BeautifulSoup
import requests
result = requests.get("https://www.moneycontrol.com/india/stockpricequote/A")

c = result.content

soup = BeautifulSoup(c)
print(soup.prettify())
soup.body.name
soup.body.text
soup.html.contents
soup.body.parent.name
soup.b.nextSibling
soup.p.previousSibling
summary = soup.find('head', {'meta': 'name'})
print(summary)

table = summary.find_all('class')


rows = table[0].findAll('tr')

for tr in rows:
	cols = tr.findAll('td')
	
	for tf in cols:
		text = tf.find(text = True)
		print (text)
		
soup.tagname.previousSibling
soup.tagname.nextSibling
paras = ' '.join([p.text + '\n' for p in soup.findAll('p')])
print(paras)
soup.findAll(id="para2")[0].text

font20 = ' '.join([p.text+'\n' for p in soup.findAll(style="font-size:20px") ])
font20
soup.findAll(['b','p'])
soup.findAll({'b': True,'p': True})

#Find all the links in a page

link = soup.findAll('a')
print(link)
link = soup.findAll('a', limit=10)  #get only the first 10 links
print(link['href']+ " is the url and "+ link.text+ "is the text")
# Let's say you want the text of the first paragraph after the first occurrence of the text "Google" 
soup.find(text="India").findNext('p').text

soup.body('p')

		