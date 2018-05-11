''' Según el libro la aplicación de ejemplo que vamos
    a realizar consiste en un programita que va a usar
    las técnicas que hemos visto de NLP para resumir
    noticias.

    Recordemos que NLTK ya tiene una buena base de datos de
    noticias antiguas, por lo que sin haber hecho esto previamente
    seguro que van por ahí los tiros.

    Para ello vamos a resumir calculando la "importancia" que tienen
    las frases dentro de las noticias.
'''

#Como las cosas buenas vienen en inglés en NLTK, pues toca hacerlo en inglés
noticia = """President Obama on Monday will ban the federal provision of some
types of military-style equipment to local police departments and sharply
restrict the availability of others, administration officials said.

The ban is part of Mr. Obama's push to ease tensions between law enforcement
and minority communities in reaction to the crises in Baltimore; Ferguson, Mo.;
and other cities.
- - -
blic." It contains dozens of recommendations for agencies throughout the country."""

#Vamos a aplicar la pipeline que vimos en 07.
import nltk

''' Para evaluar las frases se van a:
    - Enumerar
    - Realizar el Part of Speech para saber de qué tipo es cada palabra
    - Realizar el NER para encontrar e identificar entidades
    + Calcular la importancia de la frase en base al número
        de nombres (Obama, etc) y NERs que encontramos con respecto
        al total de tokens (palabras) de la frase.

    Es decir, una frase vacía sin nombres ni lugares ni nada, es poco probable que
    aporte información en una noticia. Aquí nos interesan cosas como:
        "<NOMBRE> declara la guerra al Imperio Galáctico"
    Y no cosas estilo:
        "<NOMBRE> pasea tranquilamente mientras observa la etapa
        primaveral pasar con ojos melancólicos"
'''

results = []
for numero,frase in enumerate(nltk.sent_tokenize(noticia)):
    #Tokenizamos la frase, es decir nos quedamos con las palabras.
    #Esto se ha visto en el archivo 02
    num_tokens = len(nltk.word_tokenize(frase))
    #Pos tagging de los token obtenidos, visto en el 03.
    pos_tag = nltk.pos_tag(nltk.word_tokenize(frase))
    #Contamos el número de nombres (sustantivos) que hay en la frase
    num_sustantivos = len([word for word,pos in pos_tag if pos in ["NN","NNP"] ])
    #Encontramos las entidades en la frase. Archivo 05
    entidades = nltk.ne_chunk(pos_tag, binary=False)
    num_entidades = len([chunk for chunk in entidades if hasattr(chunk, 'node')])
    score = (num_entidades + num_sustantivos) / num_tokens

    results.append((sent_no,no_of_tokens,no_of_ners, no_of_nouns,score,frase))

print(results)
