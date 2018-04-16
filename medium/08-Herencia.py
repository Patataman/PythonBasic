''' Se me había olvidado por completo hablar de herencia,
    y es que hasta hace apenas 1 mes no tuve que hacer herencia
    en Python xDDD

    Voy a suponer que conocéis el concepto de herencia,
    por lo que simplemente voy a poner aquí cómo se haría herencia entre 2 clases.'''


class A():
    def __init__(self, a_x, a_y):
        self.x = a_x
        self.y = a_y

    def printXY(self):
        print("X:{} - Y:{}".format(self.x, self.y))

''' Poco que contar aquí, es una clase llamada A, con 2 atributos (x e y)
    y un método que imprime los valores.'''

class B(A):
    def __init__(self, a_x, a_y, b_z):
        super(B , self).__init__(a_x,a_y)
        #super().__init__(a_x,a_y) es lo mismo
        self.z = b_z

    def printXYZ(self):
        print("X:{} - Y:{} - Z:{}".format(self.x, self.y, self.z))

''' Como debéis haber visto, para decir que B hereda de A, a la hora de definir la clase
    se pone A dentro de los (). Si heredase más de 1 clase, se separarían por comas: class X(1,2,3,4...)

    Para inicializar los valores heredados lo suyo es utilizar el método "super":
        super(subclass, self).method(args)

    Y como podéis ver, además he declarado un método printXYZ, sin embargo, como hereda de A, tendrá
    también el método printXY '''

a = A(1,2)
b = B(1,2,6)

a.printXY()
b.printXY()
b.printXYZ()
