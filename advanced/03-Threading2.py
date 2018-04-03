''' Algo más de uso de hilos. Si es que queréis usar hilos para algo
    Ya hemos visto como crear hilos y asignarles funciones, así que vamos
    a ir a cosas más "complicadas"

    https://docs.python.org/3/library/threading.html

    Como todo sistema de hilos deberíamos tener disponibles
    las siguientes herramientas: Cerrojos, Barreras, Semáforos, Señales (Eventos)...

    Aquí voy a poner ejemplos de Barreras y Señales que probablemente sea
    lo más útil junto quizás los cerrojos. Cualquier cosa, teneis la documentación
    o si no, pues hacéis un pull request al repo con lo que falta :)
'''

import threading
import time

#Evento para esperar y hacer cosas
event = threading.Event()

def wait_event():
    global event
    print("{}: PUES AHORA VOY A ESPERAR".format(threading.currentThread().getName()))
    #Espera a que el evento sea True. Devuelve True o False.
    #Se puede establecer un timeout en la función event.wait(X)
    ret = event.wait()
    print("{}: PUES YA NO ESPERO".format(threading.currentThread().getName()))

def wait_and_set():
    global event
    print("{}: PUES ESPERO CON TIMEOUT".format(threading.currentThread().getName()))
    #Espera 3 segundos
    ret = event.wait(3.0)
    print("{}: ACTIVO EL EVENTO".format(threading.currentThread().getName()))
    event.set()

print("######### EVENT ##########")

espera_hilo = threading.Thread(name='wait',
                  target=wait_event)

no_espera_hilo = threading.Thread(name='no-wait',
                  target=wait_and_set)

hilos = list()
hilos.append(espera_hilo)
hilos.append(no_espera_hilo)

for h in hilos:
    h.start()

while len(hilos)>0:
    for h in hilos:
        if not h.is_alive():
            hilos.remove(h)

print("###########################")
print("######### BARRIER ##########")

''' Barrier(parties, action=None, timeout=None)
    - parties: Numero de esperas hasta dejar pasar
    - action: Acción a realizar cuando deja pasar a los hilos (Se ejecuta 1 vez, no por hilo)
    - timeout: Pues un timeout, igual que en Event
'''

def foo():
    print("YOU SHALL NOT PASS!")

the_wall = threading.Barrier(2, action=foo)

def wait_wall(sec):
    global the_wall
    if sec != 0:
        print("{}: Voy a esperar {} segundos".format(threading.currentThread().getName(),sec))
    time.sleep(sec)
    the_wall.wait()
    print("{}: SOMOS LIBRES!".format(threading.currentThread().getName()))


espera_hilo = threading.Thread(name='wait_wall1',
                  target=wait_wall,
                  args=(2,))

no_espera_hilo = threading.Thread(name='wait_wall2',
                  target=wait_wall,
                  args=(0,))

hilos = list()
hilos.append(no_espera_hilo)
hilos.append(espera_hilo)

for h in hilos:
    h.start()

while len(hilos)>0:
    for h in hilos:
        if not h.is_alive():
            hilos.remove(h)

print("###########################")
