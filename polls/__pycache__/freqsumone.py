from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import urllib.request
from bs4 import BeautifulSoup

def gettext(url):
    page = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page)
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    soup2 = BeautifulSoup(text)
    text = ' '.join(map(lambda p: p.text, soup2.find_all('p')))
    return soup.title.text, text

text = "Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI."
sents = sent_tokenize(text)
print("SENT: ",sents)
print("WORD",word_tokenize(text))

url = "https://www.washingtonpost.com/powerpost/pompeo-likely-to-fail-committee-vote-but-is-all-but-assured-senate-confirmation/2018/04/23/f4dd0a28-470b-11e8-9072-f6d4bc32f223_story.html?noredirect=on&utm_term=.d8894483c4fd"
#urlmy = "https://en.wikipedia.org/wiki/Machine_(2017_film)"
text = gettext(url)
print(text)
sents = sent_tokenize(text)
print("SENT: ",str(sents))
print("WORD: ",word_tokenize(text))


import requests
res = requests.get('https://www.washingtonpost.com/powerpost/pompeo-likely-to-fail-committee-vote-but-is-all-but-assured-senate-confirmation/2018/04/23/f4dd0a28-470b-11e8-9072-f6d4bc32f223_story.html?noredirect=on&utm_term=.d8894483c4fd')
page = BeautifulSoup(res.text, 'lxml')
print(page)
text = ' '.join(map(lambda p: p.text, page.find_all('article')))
soup = BeautifulSoup(text)
text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
print(text)
sents = sent_tokenize(text)
print("SENT: ",sents)
print("WORD: ",word_tokenize(str(sents)))

url = "https://www.washingtonpost.com/powerpost/pompeo-likely-to-fail-committee-vote-but-is-all-but-assured-senate-confirmation/2018/04/23/f4dd0a28-470b-11e8-9072-f6d4bc32f223_story.html?noredirect=on&utm_term=.d8894483c4fd"
#urlmy = "https://en.wikipedia.org/wiki/Machine_(2017_film)"
text = gettext(url)
#text="hello coimbatore welcomes you. hwllo hello, hello"
print(text)

import re
t = re.sub("[^a-zA-Z]",  
                          " ",          
                          str(text))

stopWords = set(stopwords.words('english'))
words = sent_tokenize(t)
wordsFiltered = []
 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
 
print(str(wordsFiltered))

wd = word_tokenize(t)
d = defaultdict(wd)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)