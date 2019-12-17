#!/usr/bin/env python
# -*- coding: utf-8 -*-
# instalar sudo pip3 install beautifulsoup4
# instalar sudo pip3 install requests
# caso de erro ao instalar requests atualize pip3 install --upgrade pip



# Importar bibliotecas
import requests
import urllib3
from bs4 import BeautifulSoup

# Coletar a página do laudo, como pegar cada um????
page = requests.get('site')

# Criar o objeto
soup = BeautifulSoup(page.text, 'html.parser')

# Remover links inferiores caso use tabela
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Pegar todo o texto da div style13
laudo_list = soup.find(class_='style13')

# Pegar o texto de todas as instâncias da tag <p> dentro da div style13
laudo_items = laudo_list.find_all('p')

# Criar loop para imprimir todo o conteudo
for laudo_list in laudo_items:
    print(laudo_list.prettify())