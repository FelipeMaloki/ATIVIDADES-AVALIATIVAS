def numero_perfeito(numero):
    if numero <= 1:
        return False
        
    soma_divisores = 0

    for i in range(1, (numero // 2) + 1):
        if numero % i == 0:
            soma_divisores += i

    return soma_divisores == numero

print(numero_perfeito(6))   
print(numero_perfeito(28))  
print(numero_perfeito(12))  
