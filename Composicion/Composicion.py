'''
Implement, as best as you can, the identity function
in your favorite language (or the second favorite, 
if your favorite language happens to be Haskell).
'''

def identity(x):
    return x



'''
Implement the composition function in your favorite language. It
takes two functions as arguments and returns a function that is
their composition.
'''

def compose(f, g):
    return lambda x: g(f(x))


'''
Tests
'''

#Funciones base
def f1(x):
    return x + 1


def f2(x):
    return x * 2


#Composicion
f1_f2 = compose(f1, f2)

#f1.f2 compuesta ie: (x+1) * 2
#f1.f2(5) = 12

if(f1_f2(5) == 12):
    print("La funcion se compone correctamente")


#Prueba de composicion identidad
id_compose1 = compose(identity, f1)
id_compose2 = compose(f1, identity)

#Si la composicion es correcta, se debe cumplir que:
# f1 == id_compose_1 == id_compose2

if(f1(4) == id_compose1(4) == id_compose2(4)):
    print("La funcion de composicion identidad es correcta")