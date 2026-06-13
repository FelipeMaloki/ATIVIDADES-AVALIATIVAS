def soma_divisores(numero):
    soma = 0
    for i in range(1, (numero // 2) + 1):
        if numero % i == 0:
            soma += i
    return soma

def sao_amigos(a, b):

    return soma_divisores(a) == b and soma_divisores(b) == a

print(sao_amigos(220, 284))    
print(sao_amigos(1184, 1210))  
print(sao_amigos(30, 42))      