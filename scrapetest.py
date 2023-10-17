# script para obtener las categorias principales de los productos de gammaenlinea

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://gamaenlinea.com')
soup = BeautifulSoup(html.read(), 'html.parser')

# encontrar directamente las categorias
# categorias = soup.find('div', {'class': 'navigation__overflow'}).find_all('a', href=re.compile(r'^/[\w-]*/c/\d+$'))
# subCategorias = soup.find('div', {'class': 'navigation__overflow'}).find_all('div', {'class':'title'})

# datas contiene la informacion de la tabla del html que contiene las categorias y subcategorias
datos = soup.find('div', {'class':'navigation__overflow'}).find_all('li')

categoria_list = []
for data in datos:
    categoria = data.find('a', href=re.compile(r'^/[\w-]*/c/\d+$'))
    if categoria is not None:
        categoria_list.append(categoria)
# print(categoria_list)

sub_categoria_list = []
for data in datos:
    sub_categoria = data.find_all('div', {'class':'title'})
    if sub_categoria:
        sub_categoria_list.append(sub_categoria)
# print('SUB CATEGORIAS',sub_categoria_list)

for n, i in enumerate(categoria_list):
    print(categoria_list[n].attrs['title'])
    for s in sub_categoria_list[n]:
        print('*', s.get_text())
    print('*****************************')

# url_categorias_principales = []
# print('***CATEGORIAS***')

# for categoria in categorias:    
    # url_parts = categoria.attrs['href'].split('/')
    # url_categorias_principales.append((url_parts[1], url_parts[-1]))
    # print(categoria.attrs['title'], url_parts[-1])
    # print('*************************************')
    # print(categoria.attrs['title'])

# print('\n***SUB CATEGORIAS***')
# for subCategoria in subCategorias:
#     print(subCategoria.get_text())