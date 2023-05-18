""" Lista de hacks que se pueden hacer para que el código vaya más rápido.
    Algunos son por implementación del lenguaje, otros por trucos que puede hacer el intérprete

    Cosas que no le gustan a Python:
        - Metodos
        - Instanciar cosas grandes en memoria
        - Variables globales
    Probablemente me deje algunas cosas, este fichero hace como 2 años que queria haberlo hecho.
    Perdonad la falta de tildes, en el teclado que tengo ahora no hay.
"""

import time
import random


""" Metodos

Llamar repetidamente a un mismo metodo puede ser muy costoso porque implica
llamadas internas. 
"""

print("---------- Lambdas")
lista = []

t0 = time.time()
for i in range(20000):
    lista.append(1)

print(time.time()-t0)

lista = []
append_lambda = lista.append
t0 = time.time()
for i in range(20000):
    append_lambda(1)

print(time.time()-t0)

# $> 0.0005888938903808594
# $> 0.00046443939208984375
# ligeramente mas rapido

""" Instanciar cosas grandes

A Python (y en general a cualquier lenguaje) no le gusta instanciar cosas
grandes en memoria, para que quieres instanciar una lista de 200MB si la
vas a iterar de 1 en 1, por ejemplo?

Aqui entran en juego los llamados iteradores, que representan estas estructuras,
pero sin tener que instanciarlas enteras en memoria y permite recorreclas con
un uso eficiente de memoria, y por tanto, una ejecucion mucho mas rapida.

Hay tambien distintos casos que se pueden abordar:
"""

# Crear nuevas listas
print("---------- Listas comprimidas")
# 2,4,6,8,...,20
listaA = [i*2 for i in range(10)]

# "val 2", "val 4", ...., "val 20"
listaB = []

# Opcion clasica
t0 = time.time()
for i in listaA:
    listaB.append(f"val {i}")


print(time.time()-t0)

# Opcion de la gente guay
t0 = time.time()
listaB2 = [f"val {i}" for i in listaA]

print(time.time()-t0)

# $> 2.6226043701171875e-06
# $> 1.6689300537109375e-06
# Casi el doble de rapido

print("---------- Yield")
# Aproximacion clasica
def lista_larga():
    lista = [random.random() for i in range(1_000_000)]
    return lista

random.seed(1314)

count = 0
t0 = time.time()
for i in lista_larga():
    # algo
    count += i
print("suma", count, time.time()-t0)


random.seed(1314)
# Aproximacion gente guay
def lista_larga():
    for i in range(1_000_000):
        yield random.random()

count = 0
t0 = time.time()
for i in lista_larga():
    count += i

print("suma", count, time.time()-t0)

# $> suma 499800.8265087394 0.0815
# $> suma 499800.8265087394 0.0772

print("------------ variables globales")

""" Las variables globales son un engorro porque implican cambios
de contexto y quizas llamadas de sistema. Si se pueden evitar mejor.
"""

var_global = 12

def func_importante():
    global var_global

    for i in range(100_000):
        var_global += i


def func_importante2(var):
    for i in range(100_000):
        var += i

    return var

""" Como podeis ver ambas funciones hacen basicamente lo mismo, pero
si miramos el rendimiento...
"""

t0 = time.time()
func_importante()
print(var_global, time.time() - t0)

t0 = time.time()
new_var = 12
new_var = func_importante2(new_var)
print(new_var, time.time() - t0)

# $> 4999950012 0.0030002593994140625
# $> 4999950012 0.002136707305908203
