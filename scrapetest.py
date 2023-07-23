from urllib.request import urlopen
html = urlopen('https://gamaenlinea.com/BEBIDAS/Cervezas/c/003005')
print(html.read())