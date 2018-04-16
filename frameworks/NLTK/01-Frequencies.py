''' EDA significa Exploratory Data Analysis

    EDA can have many meanings, but will go with a simple case of what
    kinds of terms dominate the document. What are the topics? How frequent
    they are? The process will involve some level of preprocessing steps.
'''
import nltk
import re

from bs4 import BeautifulSoup
from urllib import request

# descarga el .html de la página
response = request.urlopen('http://python.org/')
# lee el .html y lo pasa de bytes a string
html = response.read().decode("utf8")

# Parsea el texto del html a un objeto de BeautifulShop
html = BeautifulSoup(html, 'html.parser')

''' Habría que limpiar las etiquetas del html, ya que no nos interesan
    y son basura.

    Versiones previas de NLTK tenía esta funcionalidad, pero la han eliminado
    en favor de BeautifulShop.get_text(), que parece ser que lo realiza mejor.
'''
#Limpia el html
clean_html = html.get_text()
#Separamos todas las palabras, ahora llamadas tokens
tokens = [tok for tok in clean_html.split()]
#Obtenemos la frecuencia de repetición de las palabras
frecuencia=nltk.FreqDist(tokens)
#Dibujamos una gráfica bonica con los valores ordenados
frecuencia.plot(50, cumulative=False)
