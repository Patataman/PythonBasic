# -*- coding: utf-8 -*-

'''
En "00-sintaxis" ya se ha visto un poco como se declaran variables, y no hay mucho más.
Pero para que esté todo organizado, pues se les dedica un archivo.

Al tratarse de un lenguaje de propósito general, tenemos lo más típico:
	- Enteros
	- Flotas (Números reales)
	- Booleanos (Verdarero/Falso)
	- Arrays/Listas. En Python los Arrays se llaman Listas.

Por lo tanto, aqui van algunos ejemplos:

Estos son números enteros '''
numEntero = 5
numEntero2 = 10 + 15 * 34

#Si realizamos ahora
division  = numEntero/numEntero2
#Al ser ambos números enteros, el resultado será un número entero. Si se quieren
#realizar operaciones con decimales ambos deben ser floats.

numFloat = 5.0
#En este caso numFloat2, sí que será un numero float, con valor 2.5 concretamente.
numFloat2 = 5.0/2.0

# Los booleanos se indican con True o False (la mayúscula importa)
boolean = True # <---- BIEN
#boolean = true <---- MAL
boolean2 = False
#boolean = false <---- MAL

'''Ahora lo que todo el mundo estaba esperando: Listas, que no Arrays, porque en Python no existen Arrays.
Las listas, como en la mayoría de lenguajes empiezan por el índice 0. Por lo que si tenemos un array de 4 números,
las posicíones serían: 0,1,2 y 3.


Para declarar una lista vacía. '''
lista = []
#Si queremos declarar una lista con contenido:
listaConContenido = [1,2,3,4]

'''
La estructuras de las listas son [<elemento>].
Un <elemento> a su vez pueden ser listas, y tendríamos listas encadenadas (listaception)

Dado que Python no tiene tipos de variables, en una lista podemos meter números, objetos, listas, strings...'''
listaCroqueta = ['Strings', 12, 66.6, False, None]
'''
El valor nulo o vacío, no se escribe NULL, null o nil como en otros lenguajes.
En Python es 'None' como se puede ver en la listaCroqueta.

########### Manejando un lista ###########

Para insertar, obtener o eleminar elementos de una lista, se utilizan los siguientes métodos

Insertar "Pepe" al final de la lista (Después del 4):'''
listaConContenido.append("Pepe")

#Obtener la longitud/tamaño de una lista
len(listaConContenido)

#Eliminar la PRIMERA coincidencia de un elemento específico de una lista. Si no encuentra el elemento da un ERROR.
listaConContenido.remove(2)

#Acceder a un elemento específico de la lista -> <nombreDeLaVariable>[<posicion>]
listaCroqueta[0] #Esto nos devolvería "Strings"

'''
Hay formas más avanzadas de eliminar o recuperar objetos de una lista, en todo caso se verá en los ejemplos de "medium" o "advanced"


Las listas están indizadas con números ascendentes desde el cero, pero existen listas especiales llamadas diccionarios
cuyo indice puede ser escogido.
'''

menu = {"entrante": "croquetas", "primerPlato": "croquetas de jamón", "segundoPlato": "croquetas de cocido", "postre": "croquetas de nata", "deBeber": "Albóndigas"} 

#Obtener postre
menu["postre"]
