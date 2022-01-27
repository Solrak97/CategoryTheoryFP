'''
Definir una funcion de orden superior para memoizar
una funcion y reducir tiempos de ejecucion subsecuentes
'''

#Para no hacerlo directamente con el memoize
#Standard de python voy a usar una clase a pata
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memory = {}

    def __call__(self, *args):
        if not args in self.memory:
            self.memory[args] = self.f(*args)
        return self.memory[args]


#Funcion lenta
@Memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


#Al usar Memoize es posible evitar un Stack Overflow
#Se guardan los resultados parciales en la memoria de la clase
#Entonces no es necesario calcular la profundidad
#Completa de la recursion, evitando llenar la pila con
#Llamados recursivos

for i in range(0, 5000):
    print(factorial(i))



'''
Try to memoize a function from your standard library that you
normally use to produce random numbers. Does it work?
'''

#Esto suena a mala idea ya que no hay parametro de entrada
from random import random

@Memoize
def random_memo():
    return random()

#for i in range(0, 500):
#    print(random_memo())

#Al no haber parametro se produce siempre el mismo
#Numero, rompiendo la idea del random

