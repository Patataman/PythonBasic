''' Sabed de antemano que todo esto es mentira.
    CPython NO TIENE PARALELISMO (la versión que usamos casi todos)
    debido al GIL (Global Interpreter Lock https://wiki.python.org/moin/GlobalInterpreterLock),
    que fuerza a que sólo se pueda ejecutar 1 proceso de Python a la vez, por lo que
    paralelismo real nunca tendremos.

    Ventajas del GIL:
        - Te evitas problemas de concurrencia (es 90000% más dificil debugear un programa paralelo)
        - Han añadido mejoras al intérprete para que en programas secuenciales vaya más rápido.
    Desventajas:
        - No existe paralelismo real en CPython (Python que tiene el intérprete en C)
        - Si se quiere hacer programación paralela, tienes que hacerlo en C (lo que es eficiente de verdad, vamos) y luego hacer el
          binding con Python (Numpy, OpenCV...).


    Ya visto que no hay paralelismo de verdad, vamos a ver este pseudoparalelismo.
    https://docs.python.org/3/library/threading.html '''

#Librería principal
import threading
import time #Para luego

#class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
''' Definimos un hilo que ejecutará la función indicada por "target",
    en caso de que haya que pasarle argumentos a la función lo hacemos
    mediante el argumento "args" como una tupla, es decir, args=(arg1, arg2, arg3).
    Podemos darle nombre al hilo (si nos es útil) mediante el parámetro "name"'''

# Cosas de Python, si se pone "lista"
# entiende que se le pasa 1 único valor, no una lista.
def foo(*lista):
    for x in lista:
        a = x*x*x
    print("HE ACABADO! - HILO: {}".format(threading.currentThread().getName()) )

hilo1 = threading.Thread(name="Test", target=foo, args=(range(0,100_000)) )

''' Una vez definido nuestro hilo superimportante, para ponerlo a ejecutar debemos
    usar la función "Thread.start()" '''

#El hilo comienza a ejecutar
print("Antes hilo")
hilo1.start()
''' ¿¿Pero como sabemos cuando acaba??

    Por temas de informática que no vienen a cuento, deberíamos acabar el programa
    cuando todos los hilos en ejecución hayan acabado. Sin embargo, no podemos saber
    en qué momento de su ejecución se encuentra el hilo.

    Para saber si un hilo está en ejecución, se usa "Thread.is_alive()"
    que nos avisa de si está en ejecución o ha acabado.'''

while hilo1.is_alive():
    print("ESTÁ VIVO? {}, ".format(hilo1.getName()), hilo1.is_alive())

print("Despues hilo")

''' Ahora vamos a usar varios hilos para dividir la carga de trabajo de algo muy pesado
'''

super_list = range(0,900_000)
hilos = []
hilos.append(threading.Thread(name="Super 1", target=foo, args=(super_list[:len(super_list)//2])) )
hilos.append(threading.Thread(name="Super 2", target=foo, args=(super_list[len(super_list)//2:])) )

for h in hilos:
    h.start()

while len(hilos)>0:
    for h in hilos:
        print("ESTÁ VIVO? {}, ".format(h.getName()), h.is_alive())
        if not h.is_alive():
            hilos.remove(h)
