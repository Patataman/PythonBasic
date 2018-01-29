# -*- coding: utf-8 -*- 

'''
¿Qué sería un lenguaje de programación sin métodos/funciones?
Los métodos permiten agrupar funcionalidades de código de forma
que lo tengamos más estructurado, ahorremos líneas de código y sea
más facil de leer y debugear.

La estructura es muy similar a la de otros lenguajes:

def <nombre> (<argumentos>):
	<codigo>

Si queremos que la función devuelva algún dato en la sección de código
la última sentencia debería ser "return <cosa>"

Unos ejemplos:
'''

#Método que suma dos números y los devuelve
def sumar(num1, num2):
	suma = num1 + num2
	return suma #Hacer directamente "return num1 + num2" es igual de válido.

sumaVeryImportant = sumar(1,1)
#Se puede no guardar el valor devuelto, pero entonces, ¿Para qué devolverlo?

#Método que no devuelve ningún valor, pero hace cosas
#Como hacer fibonacci hasta un número
def fibonacci(limite):
	n_1 = 0
	n = 1
	print(n_1, n,)
	while n < limite:
		print(n_1 + n,)
		aux = n
		n += n_1
		n_1 = aux
	print("") #Esto lo hago porque si no, el siguiente print es en la misma línea

fibonacci(50)


'''
Es posible también devolver múltiples valores al hacer return, por ejemplo
si estamos calculando una posición y queremos devolver la cordanada X e Y, se 
puede sin necesidad de crear un objeto, estructura o cosas raras.

Este método devuelve una posición aleatoria
'''
def getPos():
	return 25, 30

#Para recuperar ambos valores:
posX, posY = getPos()

print(posX, posY)

#si sólo se guarda en una variable se devuelve como un diccionario, el cual puede
#ser tratado como una lista.

posXY = getPos()
#Si hacemos posXY[0] obtenemos 25 y posXY[1] es 30
print(posXY[0], posXY[1])

'''
También se puede hacer recursividad en los métodos, lo cual no requiere ninguna ciencia
para hacerlo. Simplemente llamais al método por su nombre dentro del mísmo método y solucionado.

Eso si, cuidado con los bucles ♪ Balance is the key ♪



Por último, los métodos aceptan valores por defecto. Esto es tremendamente útil cuando tenemos
una función que puede servir para varias situaciones (como el constructor de un objeto (siguiente ejemplo))

Ojo, esto hace que los parámetros sean opcionales, asi que si se quiere un valor OBLIGATORIO, SE PONE DE LOS
PRIMEROS.
'''

def multiValues(valObligatorio, val1 = 20):
	print(valObligatorio+val1)

#Si hacemos multiValues(20) imprimirá 40.
#Si hacemos multiValues(20,0) imprimirá 20