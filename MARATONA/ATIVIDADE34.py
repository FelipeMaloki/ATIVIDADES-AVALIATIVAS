def listas(lista1, lista2):
    resultado = []
    for item in lista1:
        if item in lista2 and item not in resultado:
            resultado.append(item)
    return resultado

print(listas([1, 2, 3, 4], [3, 4, 5, 6]))

