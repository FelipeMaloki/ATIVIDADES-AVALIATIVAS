def somas(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10  
        numero = numero // 10  
    return soma

print(somas(12345)) 
