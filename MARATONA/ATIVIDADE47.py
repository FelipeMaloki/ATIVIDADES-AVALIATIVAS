def soma_acumulada(lista):
    resultado = []
    soma_atual = 0
    
    for numero in lista:
        soma_atual += numero
        resultado.append(soma_atual)
        
    return resultado

print(soma_acumulada([1, 2, 3, 4])) 
