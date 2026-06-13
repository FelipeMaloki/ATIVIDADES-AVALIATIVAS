def cortar_lista(lista, posicao):
    resultado = []
    
    for i in range(posicao + 1):
        resultado.append(lista[i])
        
    return resultado

print(cortar_lista([1, 2, 3, 4, 5], 2))  