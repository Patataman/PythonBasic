''' La pipeline, es decir, el conjunto de pasos a seguir
    para extraer información coherente de frases y esas
    cosas siguen los siguientes pasos (según el libro en
    el que me baso para hacer esto)

    Texto original
     |
     V
    Tokenización de las palabras (Archivo 02)
     |
     V
    PartOfSpeech (Archivo 03)
     |
     V
    Detección de entidades-NER (Archivo 05)
     |
     V
    Extracción de relaciones (Este archivo)

    Y ya tendríamos nuestras relaciones. A ver si es verdad.

    Para ello, NLTK ya viene con un conjunto de documentos del New York Times
    donde podemos buscar cosas.
'''

import nltk
import re

nltk.download('ieer')

#Expresión regular con la que buscar las relaciones, viene siendo:
# <cualquier_cosa> in <LOC>
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
#New York Times del 15 - 03 - 1998
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
        print(nltk.sem.rtuple(rel))
