# -*- coding: utf-8 -*-

'''
Como ya se ha visto en ejemplos anteriores cuando queremos mostrar algo por pantalla
se utiliza el comando "print <texto>" haciendo uso de ello podemos imprimir de distintas formas
'''

#Forma básica

print("hola")
a = "hola"
print(a)
print("Para concatenar valores como "+a+"se usa el +")

#Reemplazando valores (varias formas)

#En orden
b = "Ola k ase"
print("{} o tambien: {}".format(a, b))
#Por la posición

print("{0} o tambien: {1}".format(a,b)) #Imprimirá "hola o tambien: ola k ase"
print("{0} o tambien: {1}".format(b,a)) #Imprimirá "ola k ase o tambien: hola"

#Imprimir varios valores
for i in range(0,10):
	print(i,i*10)

#También se pueden limitar el número de decimales o imprimir en formato de tabla, pero no es necesario
#conocerlo, cualquier cosa: https://docs.python.org/2/tutorial/inputoutput.html?highlight=input%20output

'''
Para leer datos desde el teclado se utiliza la función input.
Recibe como parámetro el mensaje que se quiere mostrar por pantalla (si es que se quiere).

Esta función además interpreta el contenido que introducimos (número, string o boolean). 
'''

a = input("Dime un número\n")
print(type(a))
a = input("It's over, isn't it?\n Y ahora un string\n")
print(type(a))

#Si queremos guardar el valor introducido, simplemente hay que asignar el resultado a una variable: a = input()