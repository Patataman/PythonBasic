''' Wrapping and cleasing se refiere a...

    Limpieza de datos y formateo principalmente:
        Eliminar preprosiciones, etiquetas (en html), obtención
        de lexemas, etc...

    ------------->>>>>> IMPORTANTE

    Can we perform other NLP operations after stop word removal?

    No; never. All the typical NLP applications like POS tagging, chunking,
    and so on will need context to generate the tags for the given text.

    Once we remove the stop word, we lose the context.

    <<<<<<<<-----------------

    #######################
    # Separando en frases #
    #######################

    Muchas veces el texto será muy largo, para análisis de texto es
    recomendable separarlo en frases (vamos, split(".")). NLTK nos permite
    hacer esto por defecto
'''

from nltk import download
from nltk.tokenize import sent_tokenize
#Hace uso de un paquete llamado punkt que es necesario
#descargar previamente. Si ya se tiene bajado, no hace nada
download('punkt')

frases = 'Esta frase no es muy larga. Esta frase es la leche de larga colegatronco, amigo, compañero!'
frases_separadas = sent_tokenize(frases)
print(frases_separadas)

''' En caso de que necesitemos separar la frase por un caracter concreto, podemos
    usar: https://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.punkt.PunktSentenceTokenizer
'''

'''########################
   # Tokenizando un texto #
   ########################

    Es decir, obteniendo la entidad mínima con significado,
    normalmente palabras.
'''

from nltk.tokenize import regexp_tokenize
#Nos quedamos sólo con texto, también podríamos
#incluir números
tokens = regexp_tokenize(frases, '\w+')
print(tokens)

'''########################
   # Obteniendo el lexema #
   ########################

   https://www.nltk.org/api/nltk.stem.html

   Conocido como stemming.

   Cuando analizamos textos, nos da un tanto igual el tiempo
   o la forma que posee el verbo, por ejemplo: Comer, comemos, comíamos, comeremos...
   todo al fin y al cabo indica la acción de comer, que es lo que nos interesa
   para obtener intencionalidades.

   Hay multitud de ""stemmizadores"", yo voy a coger el de español
'''

from nltk.stem.snowball import SnowballStemmer, SpanishStemmer

#Igual que con punkt hay que bajar un paquete
download('stopwords')

#Si no conocemos el lenguaje a priori.
#SnowballStemmer(language, ignore_stopwords=False)
spanish_stem = SnowballStemmer("spanish", True)

# Si conocemos el lenguaje de antemano, podemos importarlo directamente
#SpanishStemmer(ignore_stopwords=False)
spanish_stem = SpanishStemmer(True)
print(spanish_stem.stem("Comiendo"),spanish_stem.stem("Bailando"), spanish_stem.stem("bailar"), spanish_stem.stem("estantería"))

'''################################
   # Obteniendo el verbo original #
   ################################

   Conocido como lemmatization.

   NLTK no tiene esto en español, solo inglés.
'''

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
#Igual que con punkt hay que bajar un paquete
download('wordnet')

''' Parece que en versiones actuales hay que indicar
    su uso dentro de la frase: verbo, adjetivo, sustantivo...

    a -> Adjetivo
    v -> Verbo
    n -> Nombre
    r -> Adverbio
'''
wlem = WordNetLemmatizer()
print(wlem.lemmatize("going", pos=wordnet.VERB),
        wlem.lemmatize("running", pos=wordnet.VERB),
        wlem.lemmatize("boring", pos=wordnet.VERB))
#Aunque aquí realmente boring es un adjetivo :(


'''###########################
   ######## Stop words #######
   ###########################

   Eliminar palabras no útiles como preposiciones, etc.
   NLTK viene ya con listas de palabras para 22 idiomas (español incluido)
'''

from nltk.corpus import stopwords
#Definimos el idioma
stoplist = stopwords.words('spanish')

#Frase con mucha basura
test_text = "El a ante con contra desde en un a el la o y puede que no jamón"
#Se tokeniza la frase y se compara cada palabra con la lista de stopwordsself
#Nos quedamos con la lista limpia
clean_text = [word for word in regexp_tokenize(test_text, '\w+') if word.lower() not in stoplist]
print(clean_text)

'''###########################
   # Eliminar palabras raras #
   ###########################

   Por que no ayuda tener nombres o palabras muy cortas/largas
'''

from nltk import FreqDist
# Se calcula la distancia entre las repeticiones
# de cada palabra, de forma que si no es frecuente
# es decir, una palabra rara, se quitará.
frecuencia_distancia = FreqDist(tokens)
raras = frecuencia_distancia.hapaxes()
limpieza_raras = [ word for word in tokens  if word not in raras]

print(tokens)
print(limpieza_raras)
