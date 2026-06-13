def soma(lista):
    soma = 0
    for indice, numero in enumerate(lista):
        if indice % 2 == 0:  
            soma += numero
    return soma

print(soma([1, 2, 3, 4, 5, 6]))  
