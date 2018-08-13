# For Python 2 compatibility.
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
if __name__ == '__main__':
    
from bs4 import BeautifulSoup
import requests

redditFile = requests.get("http://www.reddit.com")
html_source = redditFile.text


soup = BeautifulSoup(html_source)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))
    
    
from bs4 import BeautifulSoup
import requests
# Use the requests module to obtain a page
res = requests.get('https://www.codechef.com/problems/easy')

# Create a BeautifulSoup object
page = BeautifulSoup(res.text, 'lxml') # the text field contains the source of the page

# Now use a CSS selector in order to get the table containing the list of problems
datatable_tags = page.select('table.dataTable') # The problems are in the <table> tag,

# with class "dataTable"
# We extract the first tag from the list, since that's what we desire
datatable = datatable_tags[0]

# Now since we want problem names, they are contained in <b> tags, which are
# directly nested under <a> tags
prob_tags = datatable.select('a > b')
prob_names = [tag.getText().strip() for tag in prob_tags]
print(prob_names)

#prob_names = [ ]
#for tag in prob_tags
#    prob_names.append(tag.getText().strip())
