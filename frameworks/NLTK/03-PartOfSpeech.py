''' Este apartado consiste en realizar un análisis
    sintáctico a las frases que tenemos. Donde está más
    trillado este proceso y existen un mayor número de ejemplos
    es el inglés, así que vamos a hacer esto en inglés.

    El significado de las siglas que nos van a salir son
    (con el tagset por defecto de nltk):

        NNP, Proper noun, singular
        NNPS, Proper noun, plural
        PDT, Pre determiner
        POS, Possessive ending
        PRP, Personal pronoun
        PRP$, Possessive pronoun
        RB, Adverb
        RBR, Adverb, comparative
        RBS, Adverb, superlative
        RP, Particle
        SYM, Symbol (mathematical or scientific)
        TO, to
        UH, Interjection
        VB, Verb, base form
        VBD, Verb, past tense
        VBG, Verb, gerund/present participle
        VBN, Verb, past
        WP, Wh-pronoun
        WP$, Possessive wh-pronoun
        WRB, Wh-adverb
        #, Pound sign
        $, Dollar sign
        ., Sentence-final punctuation
        ,, Comma
        :, Colon, semi-colon
        (, Left bracket character
        ), Right bracket character
        ", Straight double quote
        ', Left open single quote
        ", Left open double quote
        ', Right close single quote
        ", Right open double quote
'''

import nltk
from nltk.tokenize import regexp_tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

#https://www.nltk.org/api/nltk.tag.html?highlight=pos_tag#nltk.tag.pos_tag
#Frase
s = "I was watching TV"

#Se tokeniza para poder ser analizada
print(regexp_tokenize(s, '\w+'))
#pos_tag(tokens, tagset=None, lang='eng')
#aunque podamos cambiar luego el idioma a 'esp' o 'spa', no funciona con español
print(nltk.pos_tag(regexp_tokenize(s,'\w+'), tagset="universal"))
