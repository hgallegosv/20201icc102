# condicion de salida, base, inicial

# Funcion de recursion, llamada a si mismo


# ejercicio
def foo(s):
 if len(s) == 1:
  print(s)
 else:
  print(s)
  s = s[1:]
  foo(s)

foo('hola mundo')

print()
# ejercicio suma
# a + b
# a + 1 + 1 + 1 + .. + 1
#    |------- b--------|


""" Suma recursiva"""
def suma(a, b):
    if b == 0:
        return a
    else:
        return 1 + suma(a, b-1)

print(suma(21, 3))

# suma(21, 3)             | 24
# 1 + suma(21, 2)         | 1 + 23
#     1 + suma(21, 1)     |     1 + 22
#         1 + suma(21, 0) |         1 + 21
#             21          |             21


# ejercicio 2
# suma de cuadrados
# n = 5
# suma = 1*1 + 2*2 + 3*3 + 4*4 + 5*5
# suma(1) = 1
# suma(2) = 1 + 4
# suma(3) = 1 + 4 + 9
# suma(4) = 1 + 4 + 9 + 16
# suma(4) = suma(3) + 16
# suma(n) = suma(n-1) + n*n


def suma_cuadrados(n):
    if n == 1:
        return 1
    else:
        return suma_cuadrados(n-1) + n*n

print(suma_cuadrados(5))
print(suma_cuadrados(6))
print(suma_cuadrados(7))


print()
# factorial
# factorial(5) = 5 * 4 * 3 * 2 * 1
# factorial(4) = 4 * 3 * 2 * 1
# factorial(1000) = 1000 * 999 * 998 ...* 2 * 1
# factorial(n) = n * factorial(n-1)
def factorial(n):
 if n == 1:
  return 1
 else:
   return n * factorial(n-1)

print(factorial(5))
print(factorial(4))

print()
# ejercicio 2
# a^b = a * a * a * a .. * a
#       |---- b veces -----|
# potencia(5,0) = 1
# potencia(5,1) = 5
# potencia(5,2) = 5*5
# potencia(5,3) = 5*5*5
# potencia(5,4) = 5*5*5*5
# potencia(5,4) = 5 * potencia(5,3)
# potencia(a,b) = a * potencia(a, b-1)

# condicion base
#
# llamada a recursion
def potencia (a, b):
  if b == 0:
    return 1
  else:
    return a * potencia(a, b-1)

print(potencia(2, 3))

# ejercicio 3
# con indices
#    i    0   1   2  3   4
# lista = [23, 45, 24, 65, 34]

# llamada a la recursion
# mayor(lista, 0)
# lista[0] comparado mayor del resto de la lista
#                    mayor(lista, 1)

# mayor(lista, indice)
# acaba cuando indice es igual al tamaño de la lista - 1

# condicion base
# mayor de la lista con un solo elemento es el elemento


def mayorLista(lista, indice):
    if len(lista) - 1 == indice:
        return lista[indice]
    else:
        temp = mayorLista(lista, indice+1)
        if lista[indice] > temp:
            return lista[indice]
        else:
            return temp

lista = [23, 45, 24, 65, 34]
print(mayorLista(lista, 0))


def mayorLista2(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        temp = mayorLista2(lista[1:])
        if lista[0] > temp:
            return lista[0]
        else:
            return temp

lista = [23, 45, 24, 65, 34]
print(mayorLista2(lista))
