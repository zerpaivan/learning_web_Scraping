# script para obtener el nombre de los productos y su precio
# de la pagina principal.
import requests
from bs4 import BeautifulSoup

response = requests.get('https://vallearriba.elplazas.com/')
soup = BeautifulSoup(response.text, 'html.parser')
products_details = soup.find_all('div', {'class': 'product-item-details'})

for product  in products_details:
    print(product.find('a', {'class':'product-item-link'}).get_text())
    print(product.find('span', {'class':'price'}).get_text())

#  el id del producto o sku se encuentra en el link class = product-item-link