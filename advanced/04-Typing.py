''' Python es un lenguaje no tipado, excepto en una pequeña región
    de la Galia que todavía resiste al invasor desde hace años, conocido
    como modulo "typing" (desde el 3.5).

    Bueno, realmente sigue siendo no tipado, pero ./shrug
    https://docs.python.org/3/library/typing.html
'''

#Función que recibe un string y devuelve un string
def greeting(name: str) -> str:
    return 'Hello ' + name


print(greeting("Pepe"))
