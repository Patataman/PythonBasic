# -*- coding: utf-8 -*-

'''
Las clases sirven para agrupar información, de forma similar a los métodos.
Concretamente en la Programación Orientada a Objetos sirven para representar...
OBJETOS!.

Si queremos representar por ejemplo un cubo, una mesa, un robot... Combiene usar
clases en vez de atributos separados.

No voy a indagar mucho más en teoría sobre POO, simplemente me voy a centrar en la
sintaxis y peculiaridades en Python.
'''


'''
Para definir una clase se usa la sentencia 

class <nombre>:
	<cosas de la clase>

Por ejemplo, vamos a representar un cohete.
'''

class Rocket:

	#Aqui podemos definir los atributos del cohete y sus valores por defecto.
#	combustible = 0
#	velocidad = 0
#	altura = 30 #metros
#	punta = "puntiaguda" #Porque si no es puntiaguda no explota, todo el mundo lo sabe.

	'''
	Bien, ya tenemos nuestra clase, ¿y ahora que?
	Bueno, todavía faltan un par de cosicas. Por ejemplo, ¿donde está el constructor de la clase?
	'''

	#El constructor se define con
	def __init__(self):
		#Aqui también se pueden definir los atributos del cohete, en vez de al comienzo.
		self.combustible = 20
		self.velocidad = 3000 #km/h
		self.altura = 30
		self.punta = "redonda" #Este cohete ya no va a explotar :(

	#También puede recibir varios parámetros si queremos definir valores nosotros mismos.
	'''
	UN MOMENTO. QUE NARICES ES ESO DE self >:(

	Self es un parámetro que se refiere a la propia clase y:
	- Hay que pasarlo como 1º parámetro en todos los métodos definidos dentro de clases.
	- Si hubiesemos definido los atributos al comienzo no haría falta, pero como Python es mágico
	  algunas de sus peculiaridades es poder definir atributos al "vuelo". Por eso dentro del init
	  se usa self.combustible, etc...
	- Siempre que nos refiramos a un atributo de la clase, dentro de la misma hay que usar self, de
	  igual forma con los métodos
	'''

	#Método que hace despegar el cohete y dice si llega a X distancia. Supongamos que gasta 1 de
	#Combustible cada 100 de distancia
	def despegue(self, distancia):
		while self.combustible > 0 and distancia != 0:
			self.combustible -= 1
			distancia -= 100

		if distancia <= 0:
			print("Misión exitosa!")
			#o return True y luego hacer un If-Else
		else:
			print("Mejor vuelve al Kerbal Space Program...")
			#o return False y luego hacer un If-Else

	#Hay otros muchos métodos propios, como el destructor, pero para quien tenga más interés:
	#https://docs.python.org/2/reference/datamodel.html#basic-customization
	
cohete1 = Rocket()
cohete1.despegue(5000)