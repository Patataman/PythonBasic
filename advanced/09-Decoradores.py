""" Los decoradores son funciones que se puede llamar de forma "automática" sobre
    otras funciones. Muy útiles cuando se quiere realizar algo repetitivo sobre
    múltiples funciones (comprobación de credenciales, limpieza de ficheros...)
"""

# Creamos la función con la que vamos a definir el decorador
# Recibe como argumento (automático) la función que se decora
def mi_decorador(func):
    # Función wrapper donde ocurre la lógica y recibe los argumentos
    # de la función que estamos decorando
    def wrapper(*args):
        print("Antes de la función")
        res = func(*args)
        print("Después de la función")
        return res
    return wrapper

@mi_decorador
def sumar(a, b):
    return a + b

print(sumar(2,4))

# Obviamente, si sabemos lo que vamos a recibir como argumentos
# Podemos hacer modificaciones antes de llamar a la función

def mi_decorador2(func):
    # Función wrapper donde ocurre la lógica y recibe los argumentos
    # de la función que estamos decorando
    def wrapper(*args):
        a, b = args
        a += 2
        b *= -1
        res = func(a, b)
        return res
    return wrapper

@mi_decorador2
def sumar2(a, b):
    return a + b

# Como a += 2 y b *= -1, si a = 2 y b = 4, el resultado es 0
print(sumar2(2,4))
