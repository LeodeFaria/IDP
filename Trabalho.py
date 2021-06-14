#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 18:59:45 2021

@author: leodefaria
"""

# importação de bibliotecas

# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError
# import ssl
import pandas as pd
# from bs4 import BeautifulSoup
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np




# importação de dados
# base original: DADOS ABERTOS - Registros de Vacinação COVID19 - UF: DF
# https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/PNI/vacina/uf/2021-06-12/uf%3DDF/part-00000-e7b5a3a9-bb01-40f5-aa63-d3bd2cfe2507.c000.csv
df = pd.read_csv('/Users/leodefaria/Downloads/part-00000-e7b5a3a9-bb01-40f5-aa63-d3bd2cfe2507.c000.csv', sep=';')
