from functools import reduce

def ej2(lista):
    resultado = list(filter((lambda x: x % 2), lista))
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado)
    print(resultado)

lista = list(range(100))

ej2(lista)


# lista = [1, 2, 4, 5, 7, 11, 25, 46, 76, 87, 33, 22]
# def buscar(x):
#     if x % 2 != 0:
#         return True
#     return False
#
# def sumaImpares(a, b):
#     return a + b
#
# impares = filter(buscar, lista)
# print(list(impares))
# lista2 = impares
#
# sumatorio = reduce(sumaImpares, lista2)
# print(sumatorio)