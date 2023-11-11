import requests
from bs4 import BeautifulSoup

class Content():
    """Clase base comun para todos los articulos/paginas"""

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    
    def the_print(self):
        """funcion flexible para mostrar en el terminal"""
        print(f'url: {self.url}')
        print(f'title: {self.title}')
        print(f'body: {self.body}')

class Website():
    """contiene info acerca de la estructura sel sitio web"""
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler():

    def getPage(self, url):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(response.text, 'html.parser')
    
    def safeGet(self, pageObj, selector):
        """
        funcion de utilidad para obtener un string de un 
        objeto Beautifulsoup y un selector. Devuelve una cadena 
        vacia si no se encuentra ningun objeto.
        """
        seletedElement = pageObj.select(selector)
        if seletedElement is not None and len(seletedElement) > 0:
            return '\n'.join([elem.get_text() for elem in seletedElement])
        
        return ''
    
    def parse(self, site, url):
        """Extrae el contenido desde la url dada"""
        soup = self.getPage(url)
        if soup is not None:
            title = self.safeGet(soup, site.titleTag)
            body = self.safeGet(soup, site.bodyTag)
            if title!='' and body != '':
                content = Content(url, title, body)
                content.the_print()

crawler = Crawler()
siteData = [
['OReilly Media', 'http://oreilly.com','h1', 'section#product-description'],
['Reuters', 'http://reuters.com', 'h1','div.StandardArticleBody_body_1gnLA'],
['Brookings', 'http://www.brookings.edu','h1', 'div.post-body'],
['New York Times', 'http://nytimes.com','h1', 'p.story-content']
]


websites = []

for n, row in enumerate(siteData):
    websites.append(Website(row[0], row[1], row[2], row[3]))
    print(websites[n].name, websites[n].url, websites[n].titleTag, websites[n].bodyTag )

crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')
     

            
