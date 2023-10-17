# from urllib.request import urlopen

# html = urlopen('https://gamaenlinea.com/ALIMENTOS-FRESCOS/Productos-del-Campo/Verduras-Legumbres/PAPA-EN-BANDEJA-1-KG/p/25001203')
# print(html.read())

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('https://gamaenlinea.com/ALIMENTOS-FRESCOS/Productos-del-Campo/Huevos/HUEVOS-PUROVO-ESTUCHE-12-UN/p/10025442')
# soup = BeautifulSoup(html.read(), 'html.parser')
# print(soup.find('div', {'class':'name'}).get_text())

from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
    html = urlopen('http://rataelmas.com')
except URLError as e:
    print('ha ocurrido un error ', e)