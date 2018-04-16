''' Python es un lenguaje no tipado, excepto en una pequeña región
    de la Galia que todavía resiste al invasor desde hace años, conocido
    como modulo "typing" (desde el 3.5).

    Bueno, realmente sigue siendo no tipado, pero ./shrug
    https://docs.python.org/3/library/typing.html

    Realmente no "tipa" nada este módulo, si no que permite indicar
    qué tipo de dato esperamos de forma que sea todo más legible y entendible.
    Todo sigue quedando en el lado del desarrollador para asegurarse que
    las cosas se reciben como deben
'''

# Función que recibe un string y devuelve un string
def greeting(name: str) -> str:
    if type(name) != str:
        return "No no no, mal, string bien."
    return 'Hello '.format(name)

print(greeting("Pepe"))
print(greeting(12)) #Funciona, pero no debería ser un string

from threading import Thread

''' Función que recibe cosas y devuelve un entero.
    Como veis se puede indicar objetos como argumento
    y de igual forma como resultado
'''
def foo(cosa1: int, cosa2: Thread, cosa3) -> int:
    return cosa1

''' Podemos crear "alias" de objetos o tipos para ahorrarnos
    texto y ser un poco más descriptivos
'''

from typing import List, Tuple

class Fruta():
    pass

#Por convenio los alias empiezan en mayúscula
Cesta = List[Fruta]
Compra = List[Cesta]

def compra(elem1: Cesta, elem2: Cesta) -> Compra:
    return [elem1, elem2]

cesta_falsa = [Fruta]*5
print(compra(cesta_falsa, cesta_falsa))

''' O incluso crear nuevos tipos! D:
    MENUDA BRUJERÍA
'''

from typing import NewType

#Realmento esto al final funciona como un alias xDD
Droga = NewType('Droga', str)

coca: Droga = Droga("Cocaina")
coco = Droga("Cocaina2")
print(coco)
print("Tipo: {}".format(type(coca)))    #Imprime "str" ya que hemos dicho que Droga va a ser str.
farlopa: Droga = Droga("Farlopa")

def goToJail(pruebas: List[Droga]) -> str:
    if len(pruebas) > 0:
        return "A la cárcel!"
    else:
        return "Está limpio"

print(goToJail([coca, farlopa]))
