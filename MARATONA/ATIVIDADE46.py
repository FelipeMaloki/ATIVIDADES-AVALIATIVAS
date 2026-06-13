def mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    if n % 2 != 0:
        return lista_ordenada[meio]
    else:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2

print(mediana([1, 2, 3, 4, 5]))  
print(mediana([1, 2, 3, 4]))     
