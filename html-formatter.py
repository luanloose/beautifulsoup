#!/usr/local/bin/python3
# -*- coding: latin-1 -*-

import os
import codecs
from bs4 import BeautifulSoup

# libraries: html5lib

report_in = "/Users/luan/Documents/5.html"
report_out = "/Users/luan/Documents/report_5.txt"

report_temp = "/Users/luan/Documents/t_5.html"

# le o conteudo do arquivo
#reader = codecs.open(report_in, 'r', 'latin-1')

# cria o objeto BeautifulSoup
#soup = BeautifulSoup(reader, 'html5lib')

with codecs.open(report_in, 'r', 'latin-1') as report_file:
    soup_obj = BeautifulSoup(report_file, 'html5lib')

    # get the content of the report
    #report_text = soup_obj.get_text()

    # Reestrutura o HTML com código válido
    report_text = soup_obj.prettify()


# Grava o conteudo de report_text no arquivo temporario
# w_temp = Arquivo temporário para gravação
with codecs.open(report_temp, 'w', 'UTF-8') as w_temp:
    w_temp.write(report_text)


#writer = open(report_temp, 'w')

#writer.write(report_text)
#writer.flush()
#writer.close()

r_text = ""

# Remove os espaços em branco do começo e final de cada linha
# r_temp = leitura do arquivo temporario
#with codecs.open(report_temp, 'r', 'UTF-8') as r_temp:
#	for line in r_temp:
#		r_text = r_text + line.lstrip()


with codecs.open(report_temp, 'r', 'UTF-8') as r_temp:
    soup = BeautifulSoup(r_temp, 'html5lib')

    r_text = soup.get_text()


with codecs.open(report_out, 'w', 'UTF-8') as w_file:
    w_file.write(r_text)


#f_writer = codecs.open(report_temp, 'w', 'utf-8')

#f_writer.write(r_text)
#f_writer.flush()
#f_writer.close()
