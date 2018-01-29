# -*- coding: utf-8 -*-

'''
Los tenrarios son sentencias if acortadas que aunque no hacen 
nada nuevo, si facilitan mucho la lectura y al final son muy
útiles.

Python utiliza los tenrarios de igual forma que la mayoría de lenguajes:
<si se cumple> if (condicion) else <si no se cumple>

De esta forma podemos ahorrarnos unas cuantas líneas de código en sentencias
muy tontas como:
	 if a>10
	 	b = a*10 - 23
'''

a = 10
variable = "Stronger than you" if a > 10 else "Made of l-o-o-ve"

print("Ternario:"+variable)

#El equivalente a las sentencias típicas sería:
a=11
if a > 10:
	variable = "Stronger than you"
else:
	variable = "Made of l-o-o-ve"

print("If: "+variable)
#Parece una tontería, pero pasar de 4 a 1 línea ayuda mucho cuando el código empieza a crecer.
#Funcionan exactamente iguales y uno puede vivir su vida sin conocerlos, pero por si acaso, aqui están.