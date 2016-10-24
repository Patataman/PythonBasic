# -*- coding:utf-8 -*-

'''
Imaginaos que estamos en un proyecto grande y tenemos separados en ficheros
las clases (como debería hacerse xD).

Necesitamos nuestro cohete del ejemplo 02 para ir a la Luna, asique vamos a "cogerlo".
Como no se debería comenzar los nombres de clases con números, lo he metido en una carpeta llamada
Clases y le he cambiado el nombre.


from Clases import Rocket #Aqui el nombre del .py
#Bien, ya tenemos todo el fichero Rocket.py, incluyendo sus clases

#Para acceder a la clase cohete habría que hacer Rocket.Rocket, pero es muy engorroso
'''

#Otra forma, si no queremos importar TODO lo que tiene el fichero es "filtrar" más
from Clases.Rocket import Rocket
aLaLuna = Rocket()
aLaLuna.despegue(300)

'''
Si alguien se ha fijado, hay un nuevo fichero, llamado "__init__.py". Sin ese fichero
Python no sabría que debe mirar ahí y buscar clases. Por lo que si se intenta importar 
algo de una carpeta sin el "__init__.py" dará error.

En caso de que querramos importar algun paquete de Python, como OS:
'''

import os #Y ale. Si queremos afinar un poco más, igual que arriba: from <sitio> import <lo que queremos>