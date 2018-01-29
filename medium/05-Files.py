# -*- coding: utf-8 -*-

'''
Este fichero pretende ser una breve introducción sobre como
abrir o escribir en ficheros. 
Para más info: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
'''

''' Para abrir un fichero hay que usar la función open(ruta al fichero, [modo])
La ruta puede ser absoluta o relativa, es preferible usar la relativa siempre.
Los modos admitidos por Python:
- r: lectura (POR DEFECTO)
- w: escritura, machacando si existía algo
- a: Añade al final del fichero
- r+/w+/a+: Cualquiera de los anteriores y un + implica: lo que hacía, mas poder leer y escribir

Vamos a leer el README por no llenar la carpeta de ficheros
'''

readme = open("README.md", 'a+') #a+ porque quiero leer y escribir al final

#Ahora hay varias formas de leer el fichero, de golpe:
print(readme.read())

readme.seek(0) #Devuelve el puntero de posición al comienzo 
			   #(Cosas internas de funcionamiento de lectura/escritura de ficheros)

#Leer línea a línea (separa por saltos de línea '\n')
for linea in readme:
	print(linea,)
readme.seek(0)

#Ya sabemos leer nuestro fichero, ahora sólo queda escribir en él.
#Vamos a añadir cualquiercosa al README
readme.write("AAAAAACHUGÜÜEEEÑAAAAA CHIBABABALAAAA")

readme.flush() 		#Para que escriba ahora en el fichero y no espere al close.
import os	   		#Para que escriba ahora en el fichero y no espere al close.
os.fsync(readme)	#Para que escriba ahora en el fichero y no espere al close.

readme.seek(0) 		#El puntero para leer y escribir es el mismo :/
print(readme.read())

readme.close() #Buena práctica el cerrar el fichero al acabar