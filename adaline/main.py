# -*- coding: utf-8 -*-

#Se importa el csv
import csv
#Se importa Adaline
from Adaline import Adaline

#Se cogen los ficheros y los datos
fichero = open('datosEntrenamiento.csv', 'r')
datosFichero = csv.reader(fichero)

#Se guardan los datos en listas
datos = []
for fila in datosFichero:
	datos.append(fila)

fichero = open('datosTest.csv', 'r')
datosFichero = csv.reader(fichero)

#Se guardan los datos para test
datosTest = []
for fila in datosFichero:
	datosTest.append(fila)

rna = Adaline()
rna.train(datos)
error = rna.test(datosTest)
print "El error es de {}".format(error)
