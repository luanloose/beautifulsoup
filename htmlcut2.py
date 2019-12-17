
import requests
from bs4 import BeautifulSoup


# Coletar e analisar a primeira página
page = requests.get('site')
soup = BeautifulSoup(page.text, 'html.parser')

# Remover links inferiores
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Pegar todo o texto da div BodyText
artist_name_list = soup.find(class_='BodyText')

# Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
artist_name_list_items = artist_name_list.find_all('a')

# Criar loop para imprimir todos os nomes de artistas
# artist_name tera todas as tags e mostrara na tela
for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        print(names)