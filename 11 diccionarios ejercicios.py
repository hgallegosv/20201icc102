# ejercicio 6
cadena = "hola mundo hola pais mundo mundo feliz"

def funcion6(cadena):
    dic = {}
    palabras = cadena.split(" ")
    print(palabras)
    for palabra in palabras:
        dic[palabra] = palabras.count(palabra)

    return dic

dic = funcion6(cadena)
print(dic.items())

for elem in dic.items():
    print(elem)

for clave, valor in dic.items():
    print(clave, " = ", valor)
