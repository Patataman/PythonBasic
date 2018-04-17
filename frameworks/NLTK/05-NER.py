''' Name Entity Recognition.

    Es decir, reconocer entidades en un texto: Nombres, lugares, organizaciones...
    Esto se puede realizar con el ne_chunk de NLTK, pero para ello, el texto
    debe ser antes: separado en frases, tokenizar las frases y realizar el POS tag.

    Una vez hecho todo eso podemos pasar a aplicar el NER.
    https://www.nltk.org/api/nltk.chunk.html#nltk.chunk.ne_chunk
'''

from nltk.tokenize import regexp_tokenize
from nltk import ne_chunk
from nltk import pos_tag
from nltk import download

download('maxent_ne_chunker')
download('words')

#Claro está, NLTK trae por defecto el inglés bien pulido. El español nope.
frase = "Steven could be the main character, but Peridot is the coolest. \
        Stevonnie too, you must like Stevonnie. If not, please go to live \
        to New Jersey and leave Beach City"

frases_separadas = regexp_tokenize(frase, '\w+')
frases_tag = pos_tag(frases_separadas)
print("NLTK NER: ", ne_chunk(frases_tag, binary=False))

''' Podemos usar también un NER de Stanford, o al menos una versión del mismo
    que debería ser mejor que el de NLTK.
'''

from nltk.tag.stanford import StanfordNERTagger
stanford_ner = StanfordNERTagger('assets/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', 'assets/stanford-ner/stanford-ner.jar')
#Al igual que en el 04, aquí le pasamos todo el texto, sin separar ni nada.
#lo hará él por nosotros.
print("Stanford NER: ", stanford_ner.tag(frases_separadas))

''' Recordad que aquí buscábamos nombres, entidades, lugares, organizaciones...
    En este caso, Stanford reconoce mejor estos valores, ya que como veréis, para
    "Beach City", NLTK dice que es un nombre (de persona) y Stanford dice que es un lugar
'''
