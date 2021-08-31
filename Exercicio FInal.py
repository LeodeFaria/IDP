#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 09:57:32 2021

@author: leodefaria

Exercício para avaliação

Individual ou em grupos até 3 estudantes

Objetivo geral: capturar informações referentes a patentes nos Estados Unidos.

    1 Salvar base de dados em vários formatos ('persistência').

    2 Fazer upload ('post') do código para a internet.

    3 Apresentar relatório geral do quantitativo de patentes ano a ano ('tratamento')

(Opcional) Desenvolver boas práticas de código entregando um ('script' e 'git')

Entrega: envio para o e-mail do professor: furtadobb @ gmail.com

Link da página pastebin com o código utilizado para o exercício e o JSON salvo
Alternativamente, link do repositório público no GitHub
Relatório contendo:
Número total de arquivos zip contendo os textos das patentes no período 1997-2015
Número de arquivos por ano.
(Opcional) Gráfico

(Opcional) Código para dar download e unzip os arquivos

(Opcional) Como o resultado é pouco informativo, utilize a expressão abaixo, dentro de um loop pelas keys do dicionário, loop link a link, identifique o tamanho do arquivo e some ao total de dados para aquele ano.

with urllib.request.urlopen(link) as handler:
    output_size[key] += int(handler.getheader('Content-Length'))
Exercício do Lucas (Opcional): https://colab.research.google.com/drive/1iaBWUmibRLONO6angRjfkGUCR0ggpesg?usp=sharing

Exercício do Lucas REGEX (Opcional): https://colab.research.google.com/drive/1BNB2ovHrqHuOx20_GdmLSsvKGmUqnxwR?usp=sharing

"""

# ------------------------------------------------------------------
# Importe as bibliotecas necessárias:
# ------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup as BS
from collections import defaultdict
import os
import pickle
import json


# ------------------------------------------------------------------
# Cria a pasta de armazenamento
# ------------------------------------------------------------------

pasta = 'dados_exercicio_final'

if not os.path.exists(pasta):
    os.mkdir(pasta)

# ------------------------------------------------------------------
# Cria funções de persistência
# ------------------------------------------------------------------

def cria_json(ob, name='dados_exercicio_final/json_da_listaAnos'):
  with open(name, 'w') as outfile:
    json.dump(ob, outfile)
    print('\n**** JSON salvo com sucesso! ****')

def cria_pickle(ob, name='dados_exercicio_final/pickle_da_listaAnos'):
    with open(name, 'wb') as handler:
        pickle.dump(ob, handler)
    print('\n**** Pickle salvo com sucesso! ****')



# ------------------------------------------------------------------
# Utilize a página de referência: 
# ------------------------------------------------------------------

url_in = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'

# ------------------------------------------------------------------
# Utilize a função get da biblioteca requests:
# ------------------------------------------------------------------

pagina = requests.get(url_in)

# ------------------------------------------------------------------
# Utilize a biblioteca BeautifulSoup:
# ------------------------------------------------------------------

paginaConteudo = BS(pagina.content, 'html5lib')

# ------------------------------------------------------------------
# Sobre o resultado interpretado busque por todas as seções:
# ------------------------------------------------------------------

linksSujos = paginaConteudo.find_all('a', href=True)

# ------------------------------------------------------------------
# Faça um loop na lista de links encontrada mantendo a expressão 'href':
# ------------------------------------------------------------------

linksLimpos = [item.get('href') for item in linksSujos if 'http' in item.get('href')]

# ------------------------------------------------------------------
# Com outro loop, limpe o resultado (.zip e grant_full_text):
# ------------------------------------------------------------------

linksUteis = [item for item in linksLimpos if 'grant_full_text' in item]

# ------------------------------------------------------------------
# Separar a lista por anos.
# ------------------------------------------------------------------

listaAnos = defaultdict(list)

for ano in range(1976,2016):
  for item in linksUteis:
    if str(ano) in item:
      listaAnos[ano].append(item)

# ------------------------------------------------------------------
# Imprime o tamanho da lista de cada ano:
# ------------------------------------------------------------------

for item in listaAnos:
    print(f'O ano {item} tem tamanho {len(listaAnos[item])}')

# ------------------------------------------------------------------
# Salve o dicionário em pickle
# ------------------------------------------------------------------

cria_pickle(listaAnos)

# ------------------------------------------------------------------
# Transforme o dicionário em JSON e salve:  
# ------------------------------------------------------------------  

cria_json(listaAnos)


# ------------------------------------------------------------------
# Baixa um zip
# ------------------------------------------------------------------

name = linksUteis[0].split('/')
name = [n for n in name if 'zip' in n][0]

r = requests.get(linksUteis[0])
with open(f'{pasta}/{name}', 'wb') as handler:
    handler.write(r.content)
