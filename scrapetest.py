# script para obtener las categorias principales de los productos de gammaenlinea

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://gamaenlinea.com')
soup = BeautifulSoup(html.read(), 'html.parser')
categorias = soup.find('ul', {'class': 'nav__links nav__links--products js-offcanvas-links'}).find_all('a', href=re.compile(r'^/[\w-]*/c/\d+$'))
for categoria in categorias:
    print(categoria.attrs['title'])
    print('ID: ', categoria.attrs['href'].split('/')[-1])
# nav__links nav__links--products js-offcanvas-links