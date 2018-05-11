''' TT^TT

    TT^TT

    POR QUEEEEEEEEEE???? :_(

    Bueno... qué le vamos a hacer :'(
    Aquí vamos a analizar y generar gramáticas. Que es
    un contenido fuera de todo esto. Si os interesan las gramáticas
    aprended de compiladores, intérpretes, estudiad informática o
    mirad en esta página de la wikipedia: https://es.wikipedia.org/wiki/Gram%C3%A1tica_formal
'''

#Hay muchos tipos de gramáticas, la más fácil es una
#Gramática Libre de Contexto (Context Free Grammar)
from nltk import CFG
from nltk.parse.generate import generate

#Definimos una gramática simplona
gramatica = CFG.fromstring(""" S -> NP VP
  VP -> V NP
  V -> "mata" | "roba"
  NP -> Det N | NP NP
  Det -> "un" | "el" | "con" | "a" | "una"
  N -> "bebé" | "ladrón" | "Obama" | "perrete" | "navastola" | "navaja" | "pistola" """)

''' Esta gramática nos dejaría definir frases del estilo:
        El bebé roba a Obama
'''
#Generamos todas las producciones posibles
gramatica.productions()

#Podemos ver así todas las frases de profundidad 5
#que se podrían generar
for posible_frase in generate(gramatica, depth=5):
    print(' '.join(posible_frase))
