''' Al igual que muchos otros lenguajes, Python tiene sistemas para controlar
	los errores que pueden ocurrir a lo largo de la ejecución de un programa.

	El más típico es el par try-except (try-catch de toda la vida vamos)
	Está formado por dos bloques de código definidos con la palabra reservada: try y except.

	try:
		<código>
	except [Error al que responder]:
		<código a ejecutar con el error>

	#Más info sobre los errores y toda la pesca: https://docs.python.org/3/tutorial/errors.html
'''

#Ejemplos:
try:
	print("Ola k ase, esto funciona así que no entrará en except")
except:
	print("Como try funciona esto no se llama")


try:
	print("Error en el print" + 12)
except:
	print("Oh dios mío, error en el segundo print")

''' Podemos concatenar varias cláusulas "except" en caso de que queramos responder de distinta
	forma a las posibles excepciones con los que nos encontremos

	Para más info sobre las excepciones, mirad la página de la documentación (link más arriba)
'''

print("Multiples except 1")
try:
	print("Error en el print" + 12)
except ValueError:
	print("Error de valor: ValueError")
except TypeError:
	print("Error de tipos: TypeError")
except:
	print("Except genérico")

print("Multiples except 2")
try:
	read("pepe.json")
except ValueError:
	print("Error de valor: ValueError")
except TypeError:
	print("Error de tipos: TypeError")
except:
	print("Except genérico, ya que no hay error de archivos")


''' Con el comando "raise" podemos levantar manualmente excepciones.

	En algunos casos esto puede ser útil ya que nos puede interesar "proteger" la ejecución
	del programa con try-except e intentar arreglar el error o simplemente generar un log más detallado
	y luego levantar la excepción y finaliza la ejecución.
'''

print("Multiples except 3")
try:
	print("Aquí voy a forzar que se pare el programa")
	a = range(0,10)
	a[12]
except ValueError:
	print("Error de valor: ValueError")
except TypeError:
	print("Error de tipos: TypeError")
except:
	print("Except genérico")
	raise
