''' No tenemos porqué estar limitados a los modelos incorporados
    en NLTK, podemos importar modelos de terceros.

    Este ejemplo importa el modelo de Stanford, que se puede encontrar
    en: http://nlp.stanford.edu/software/stanford-postagger-full-2014-08-27.zip

    La documentación correspondiente: https://www.nltk.org/api/nltk.tag.html?highlight=pos_tag#nltk.tag.pos_tag

    Pese a lo dicho anteriormente y en el 04, parece que a partir de ahora se utiliza el módulo
    CoreNLP (http://www.nltk.org/api/nltk.parse.html#module-nltk.parse.corenlp) como sustituto a
    los "taggers" anteriores.
    No estoy seguro, pero digo yo que va por estos tiros, ya que si se usa el StanfordTagger, avisa
    de que está deprecado desde la 3.2.5 (última versión en momento de hacer esto).

    Sin embargo, dado que he sido incapaz de hacer funcionar el CoreNLP, pues tiro de lo que
    se va a deprecar
'''

from nltk.tag import StanfordPOSTagger
from nltk.tokenize import regexp_tokenize

#POSTagger(path_to_the_model, .jar_of_the_model (optional), encoding="utf-8")
text = "Long ago, in a galaxy far away, Naboo was under attack. \
        Their response didn't thrill us. They lock the doors and \
        try to kill us."

stanford_tagger = StanfordPOSTagger('assets/stanford/models/english-bidirectional-distsim.tagger',
                                    path_to_jar='assets/stanford/stanford-postagger.jar')
print("Stanford english: ", stanford_tagger.tag(regexp_tokenize(text, '\w+')))


''' Podemos entrenar nuestros propios "taggeadores" (a falta de mejor palabra)
    Problema: Como toda tarea de IA supervisada, requiere entrenamiento con ejemplos ya
              clasificados, ¿y quien los tiene que clasificar? Sí, tú.

    Ej: Well/UH what/WP do/VBP you/PRP think/VB about/IN the/DT idea/NN of/IN ,/, uh/UH ,/,
        kids/NNS having/VBG to/TO do/VB public/JJ service/NN work/NN for/IN a/DT year/NN ?/.Do/VBP
        you/PRP think/VBP it/PRP 's/BES a/DT ,/,

    ##########################
    ##### Default Tagger #####
    ##########################

'''

#Brown es otro corpus ya entrenado con etiquetas
from nltk.corpus import brown
import nltk

nltk.download('brown')

#obtenemos la lista de para cada palabra del corpus, su categoría (nombre, adjetivo, etc)
brown_tagged_sents = brown.tagged_sents(categories='news')

''' Para nuestro "taggeador" personalizado podemos
    comenzar tirando de uno por defecto, que asigna a todo
    la etiqueta que le digamos.
    En este caso, asigna todo como "nombres"
'''
default_tagger = nltk.DefaultTagger('NN')
#Comparamos la precisión de decir que todo es nombre
# con la clasificación del corpus
print("Default Tagger: {}".format(default_tagger.evaluate(brown_tagged_sents)))

'''
    #########################
    ###   N-Gram Tagger   ###
    #########################

    https://www.nltk.org/api/nltk.tag.html?highlight=postagger#nltk.tag.sequential.NgramTagger

    Aquí el "taggeador" coge las N palabras previas
    para clasificar correctamente la nueva palabra
'''

from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger
# we are dividing the data into a test and train to evaluate our taggers.
train_data = brown_tagged_sents[:int(len(brown_tagged_sents) * 0.9)]
test_data = brown_tagged_sents[int(len(brown_tagged_sents) * 0.9):]

#Unigram selecciona la clasificación + probable
#https://www.nltk.org/api/nltk.tag.html?highlight=postagger#nltk.tag.sequential.UnigramTagger
unigram_tagger = UnigramTagger(train_data,backoff=default_tagger)
print("Unigram Tagger: {}".format(unigram_tagger.evaluate(test_data)))
#Bigram se basa en la palabra actual y la anterior para clasificar
#https://www.nltk.org/api/nltk.tag.html?highlight=postagger#nltk.tag.sequential.BigramTagger
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
print("Bigram Tagger: {}".format(bigram_tagger.evaluate(test_data)))
#Trigram se basa en la actual, anterior y anterior a la anterior
#https://www.nltk.org/api/nltk.tag.html?highlight=postagger#nltk.tag.sequential.TrigramTagger
trigram_tagger = TrigramTagger(train_data,backoff=bigram_tagger)
print("Trigram Tagger: {}".format(trigram_tagger.evaluate(test_data)))

''' Aquí lo que se ha hecho ha sido crear 3 "taggeadores" N-Gram con un conjunto
    de datos de entrenamiento del corpus brown, que ya estaba clasificado.

    Además, se han podido combinar para que cuando un "taggeador" no sepa que hacer
    pruebe con su "taggeador" N-1 hasta llegar al por defecto de clasificarlo como NN.


    #######################
    ###  Regexp Tagger  ###
    #######################

    Otra opción para crear nuestro propio "taggeador" es recurrir
    a las queridas expresiones regulares con un RegexpTagger
'''

from nltk.tag import RegexpTagger
regexp_tagger = RegexpTagger(
         [( r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
          ( r'(The|the|A|a|An|an)$', 'AT'),   # articles
          ( r'.*able$', 'JJ'),                # adjectives
          ( r'.*ness$', 'NN'),         # nouns formed from adj
          ( r'.*ly$', 'RB'),           # adverbs
          ( r'.*s$', 'NNS'),           # plural nouns
          ( r'.*ing$', 'VBG'),         # gerunds
          (r'.*ed$', 'VBD'),           # past tense verbs
          (r'.*', 'NN')                # nouns (default)
          ])
print("Regexp Tagger: {}".format(regexp_tagger.evaluate(test_data)))

''' Visto lo anterior, podemos poner al tagger regexp como backoff
    de los N-gram creados anteriormente.

    O podríamos ponerlo 1º, pero me fio más de los preentrenados
    que de unas reglas puestas a capón.
'''

regexp_tagger = RegexpTagger(
         [( r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
          ( r'(The|the|A|a|An|an)$', 'AT'),   # articles
          ( r'.*able$', 'JJ'),                # adjectives
          ( r'.*ness$', 'NN'),         # nouns formed from adj
          ( r'.*ly$', 'RB'),           # adverbs
          ( r'.*s$', 'NNS'),           # plural nouns
          ( r'.*ing$', 'VBG'),         # gerunds
          (r'.*ed$', 'VBD'),           # past tense verbs
          (r'.*', 'NN')                # past tense verbs
          ])
unigram_tagger = UnigramTagger(train_data,backoff=regexp_tagger)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
wombo_combo = TrigramTagger(train_data,backoff=bigram_tagger)
print("Wombo-combo Tagger: {}".format(wombo_combo.evaluate(test_data)))


''' ######################
    ###  Brill Tagger  ###
    ######################

    https://www.nltk.org/api/nltk.tag.html?highlight=postagger#module-nltk.tag.brill

    Este taggeador se basa en clasificar una palabra a priori
    y con las siguientes palabras verificar si lo que se ha
    hecho está bien o mal.

    Para esto se basa en reglas, estilo: Si A y B han sido X e Y, entonces C es Z.

    De este caso no tengo ejemplo :(
'''
