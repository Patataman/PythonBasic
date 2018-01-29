''' Más formas de utilizar las listas junto con bucles.

	Acceso, creación, y esas cosas chulas que nos 
	van a ahorrar entre 3 y 5 líneas de código cada vez
'''

############## CREAR LISTAS ##################

''' Si queremos por ejemplo, copiar una lista no podemos hacer esto:
	
	$> copia = lista

	Ya que si hacemos esto estamos copiando la dirección de memoria y por tanto seguimos
	modificando "lista" al hacer cosas en "copia".

	Una posible solución sería utilizar el paquete "copy" que permite hacer "deep copy" o "shallow copy",
	pero eso mejor lo reservamos para clases, ya que aquí sería matar moscas a cañonazos.

	Entonces vamos a lo que interesa: Copiar una lista sin ser copia por referencia, si no, copia por valor
	(copiar de verdad, no la dirección de memoria).
'''

#Forma 1 - El pringao:
lista_original = range(1,100)
lista_copia = []
for i in lista_original:
	lista_copia.append(i)

# Con esto tendríamos nuestra lista copiada. Pero es mu feo y ocupa mucho, otra forma sería:
#Forma 2 - Drop the mic

lista_copia = [x for x in lista_original]

''' Y tenemos el mismo resultado. La brujería que acaba de ocurrir aquí es uno de los muchos trucos
	que tiene Python oculto. 

	[ cosa_del_for for item in <lista> ]

	Esta es la forma acortada del bucle for, se ejecuta igual que un for de toda la vida de Python,
	pero está pensado para asignaciones como la que acabamos de ver. 

	Se puede rizar mucho más el bucle y hacer virgerías muy tochas, tales como mezclar la versión
	acortada del for junto con los ternarios (03-Ternarios.py) y se crearían monstruos tales como este:
'''

#Esto genera una lista con los números pares de lista_original
lista_par = [x for x in lista_original if x%2 == 0]
#Imprime los 10 primeros elementos
print(lista_par[:10])


'''En caso de querer añadir un resultado en caso de que no se cumpla la condición (añadir un "else")
	Hay que cambiar el orden del "if".

	Esto generará una lista con "pepe" donde el número sea impar y el número si es par.
'''
lista_string = [x if x%2 == 0 else "pepe" for x in lista_original if x%2 == 0]

#Imprime los 10 primeros elementos
print(lista_string[:10])


############### ACCEDER A LISTAS #################
''' Lo acabo de utilizar y es bastante explicativo. Si queremos acceder
	por ejemplo a los primeros X elementos o a los último Y elementos, 
	podemos hacerlo sin tener que llevar mucho la cuenta de cuántos elementos 
	existen en la lista gracias al operador ":"

	Algunos ejemplos a continuación:
'''

#Acceder a los primeros X elementos: lista[:X]
print(lista_par[:5])

#Acceder a los últimos Y elementos: lista[-Y:]
print(lista_par[-5:])

#Acceder a los elementos que existen desde la posición W hasta la Z: lista[W:Z]
print(lista_par[4:8])

''' De esta forma podemos mezclar todo y hacer cosas como:
'''

#Dividir una lista en 2 mitades:
mitad1 = [i for i in lista_par[:len(lista_par)//2]]
mitad2 = [i for i in lista_par[len(lista_par)//2:]]

print(mitad1, mitad2)