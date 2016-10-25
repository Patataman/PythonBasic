# -*- coding: utf-8 -*-

import random

class Adaline:

	def __init__(self):
		self.razon = 0
		self.ciclos = 0
		self.pesos = [] #Los pesos se deben inicializar al entrenar. Ya que depende del número de atributos

	#Se entrena la red.
	def train(self, datos, razon=0.01,ciclos=300):
		self.razon = razon
		self.ciclos = ciclos
		#Se inicializan los pesos aleatoriamente
		for i in range(0, len(datos[0])):
			self.pesos.append(float(random.random()))

		#Se realizan X ciclos de entrenamiento
		for i in range(0,ciclos):
			'''
			Cada ciclo de entrenamiento consiste en recorrer
			todos los datos de entrada y actualizar los pesos
			'''
			for instancia in datos:
				#Hay que calcular el valor esperado (último de la lista)
				#Hay que hacer casting a float porque el texto es string
				valorEsperado = float(instancia[len(instancia)-1])

				#valor estimado
				y = 0.0

				#Valor de la entrada por su peso
				for Xi in range(0,len(instancia)-1):
					y += float(instancia[Xi])*self.pesos[Xi]

				y += self.pesos[len(instancia)-1]

				diferencia = valorEsperado - y

				for Wi in range(0,72):
					self.pesos[Wi] += razon*diferencia*float(instancia[Wi])

				self.pesos[len(instancia)-1] += razon*diferencia



	def test(self,datos):
		#Se repite el proceso de calcular error, pero esta vez sólo para test
		errorCuadratico = 0.0
		#Se calcula el error del archivo de test
		for instancia in datos: #Paso 6 y Paso 2
			#Valor esperado (último de la fila) Paso 3
			valorEsperado = float(instancia[len(instancia)-1])

			y = 0.0
			#Por cada Xi hasta Xn-2 (Hay que ir de 0 hasta N-2 porque N-1 es la clase)
			for Xi in range(0,len(instancia)-1):
				#Se calcula el sumatorio
				y += float(instancia[Xi])*self.pesos[Xi]
				#print float(instancia[Xi])

			#Se le suma el umbral
			y += self.pesos[len(instancia)-1]

			#Aqui se tiene el valor obtenido y hay que compararlo con el deseado
			diferencia = valorEsperado - y
			errorCuadratico += diferencia*diferencia

		#Error obtenido en Test
		return errorCuadratico/len(datos)
