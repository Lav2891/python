from __future__ import print_function
import lxml.html
import requests
def main():
    r = requests.get("https://httpbin.org")
    html_source = r.text
    root_element = lxml.html.fromstring(html_source)
    # Note root_element.xpath() gives a *list* of results.
    # XPath specifies a path to the element we want.
    page_title = root_element.xpath('/html/head/title/text()')[0]
    print(page_title)
if __name__ == '__main__': main()


def main():
    r = requests.get("https://httpbin.org")
    html_source = r.text
    root_element = lxml.html.fromstring(html_source)
    # Note root_element.xpath() gives a *list* of results.
    # XPath specifies a path to the element we want.
    page_title = root_element.xpath('//a/@href')[0]
    print(page_title)
if __name__ == '__main__': main()


from bs4 import BeautifulSoup
redditFile = requests.get("https://www.w3schools.com/")
html_source = redditFile.text
soup = BeautifulSoup(html_source)
redditAll = soup.find_all("div")
for links in soup.find_all('div'):
    print (links.get('h2'))