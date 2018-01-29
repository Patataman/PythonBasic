''' Comenzamos fuerte este apartado con las lambdas. 

	¿Qué es una lambda, a parte del logo de Half-Life?
	[1] Doc oficial: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
	[2] Doc útil también: http://www.secnetix.de/olli/Python/lambda_functions.hawk
	
	De forma coloquial: Una lambda sirve para almacenar en variables funciones para luego poder ser llamadas.
'''

''' Esto da la ventaja de poder llamar funciones de una clase en otra pasándola por argumento, o hacer
	brujerías demasiado locas para mi gusto que no voy a poner aquí y que espero que nunca veáis.
'''

#Para poder crear y usar lambdas primero necesitamos 1 función que asociar. Vamos a algo fácil:
def movimientoBrowniano(n):
	return lambda x: n**x

#HEHEHE os he engañado y es sólo una potencia, no el cálculo del movimiento Browniano (https://en.wikipedia.org/wiki/Brownian_motion)

''' Bien, ya tenemos nuestra superfunción para crear la lambda.
	La función que hemos definido tiene un poco de truco y lo voy a explicar con un ejemplo
'''

#Con esto estamos definiendo a "a" como la función n**x, siendo n=2.
a = movimientoBrowniano(2)

#Ahora podemos usar "a" como si fuese una función:
print(a(3))        #Esto devolverá 2**3 -> 8

'''De esta forma, aquí x == 3

   Otra forma de declarar lambdas más sencilla para estos casos es en una única línea.
'''

#Podemos declarar lambdas de un único argumento
a = lambda x: 2**x
#O tirar la casa por la ventana y declarar AMBOS argumentos
b = lambda x,n: n**x
print(a(4))          #Esto devolverá 16
print(b(4,2))        #Esto devolverá 16


''' Estos casos para el uso de lambdas puede ser muy tonto, pero en la referencia [2] hay ejemplos
	más útiles sobre el uso de las lambdas. 

	En este repositorio mío hay otro ejemplo útil (https://github.com/Patataman/StuffPygame/tree/master/WheelSelector)
	En ese repositorio utilizo PyGame para crear un selector de rueda donde cada cuarto de la rueda sirve para colorear
	el fondo de pantalla.
	La función de colorear el fondo de pantalla está creada en la escena y es pasada al selector haciendo uso de lambdas,
	de forma que luego cuando se hace click en uno de los cuartos de la rueda se modifica el fondo de la pantalla llamando
	a la función de coloreado DESDE el selector, no desde la escena donde está la función.

	Este ejemplo me parece más bonito a nivel de utilidad, pero no era posible de incluir aquí.
'''