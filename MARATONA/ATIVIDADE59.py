def soma_quadrados(lista):
    soma = 0
    for num in lista:
        soma += num * num
    return soma

print(soma_quadrados([1, 2, 3]))  
print(soma_quadrados([4, 5, 6]))  
