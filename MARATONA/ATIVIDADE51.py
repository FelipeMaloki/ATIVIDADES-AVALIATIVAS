def soma_impares(n):
    soma = 0
    for num in range(1, n + 1, 2):
        soma += num
    return soma

print(soma_impares(10))  
