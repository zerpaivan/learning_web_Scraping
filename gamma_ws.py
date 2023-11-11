from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://gamaenlinea.com/')
soup  = BeautifulSoup(html, 'html.parser')

a_links = soup.find_all('a', href = re.compile(r'\S+\/p\/\d+'))
for link in a_links:
    if 'href' in link.attrs:
        print(link.attrs['href'])

print(len(a_links))