# -*- coding: utf-8 -*-

'''
Python posee los dos búcles más comunes: For y While
Para indicar el condenido del bucle, se debe tabular todo el contenido del mismo,
de esta forma Python sabe que código pertenece a cada sección.

El bucle For sirve tanto como Foreach que como For típico, pero en Python realmente estamos usando un Foreach.
El bucle While es el de toda la vida. Mientras se cumpla una condición, ejecuta.

'''

#Bucle For (Foreach)

lista = [1,2,3,4,5,10]
for i in lista:
    print(i)

'''
Este código se leería: Por cada elemento 'i' de la lista haz: print <elemento>

Si buscamos recorrer una lista de forma que sólo recuperemos ciertos valores, por ejemplo
las posiciones pares, se puede hacer de dos formas:

Utilizando la función range(x,y), la cual genera una lista con los valores [x,y).
O range(x,y,[step]), que tiene un parámetro opcional que indica cuanto aumenta el valor.

Este bucle se asemeja más al bucle típico, con un índice que aumenta, sin embargo
como se ha explicado antes, range y xrange devuelven una lista con los valores, por lo
que realmente estamos usando un foreach.
'''
for i in range(0,5):
    print(lista[i])

#Esto imprimiría las posiciones de 0 a 4 de la lista (1,2,3,4 y 5)
#Lista que comienza en 0 y aumenta su valor en 2 hasta llegar a 6 (sin incluir)
for i in range(0,6,2):
    print(lista[i])

'''
Esto imprimiría las posiciones, 0, 2 y 4 (1, 3 y 5). Ya que la lista no incluye el valor límite (6).

Antes de empezar con while e if, a diferencia de otros lenguajes, los operadores AND, OR y !(not) son
distintos a la mayoría:

&& se escribe "and"
|| se escribe "or"
! se escribe "not"

Parece de sentido común, pero no acepta los otros valores.


El bucle While no tiene mucho misterio, su sintaxis es:

while <se cumple condición>:
    codigo

Este código imprime valores del 0 al 9.
'''

cont = 0
while cont < 10:
    print(cont)
    cont += 1


'''
Vistos ya los bucles, lo último que quedaría es la sentencia If.

if <condicion>:
    codigo
elif <condicion2:
    codigo2
else:
    codigo3

La parte que será siempre obligatoria en un if es su primera sentencia:
if <condicion>:
    codigo

Si queremos que se realice otro código en caso de que la condición no se cumpla, hay que usar la
parte de:
else:
    codigo3

Y si queremos evaluar una serie de condiciones, usar la sentencia elif (contracción de 'else if'):
elif <condicion2>:
    codigo2
'''

hora = "madrugada"
if hora == "mañana":
    print("Breakfast time!")
elif hora == "noche":
    print("Party time")
else:
    print("No ocurre nada bueno pasadas las 2 de la madrugada")

#En este caso se llegaría hasta la sentencia else. Pero si 'hora' fuese igual a "noche",
#se ejecutaría el código asociado a ese bloque y no se ejecutaría ninguna otra parte del if.

'''
Como en la mayoría de lenguajes, estas sentencias se pueden anidar todas las veces que se quiera,
pero se debe tener en cuenta la tabulación para que python sepa a que sentencia de control pertenecen
las instrucciones
'''
for x in range(1,20):
    for i in range(1,3):
        print(str(i) + " patata")
    if x%2 == 0:
        print(str(x) + " es par")
    else:
        if x == 5:
            print(str(x) + " por el *************")
        else:
            print(str(x) + " es impar")

    print("hemos terminado con " + str(x))

print("hemos terminado el for")

