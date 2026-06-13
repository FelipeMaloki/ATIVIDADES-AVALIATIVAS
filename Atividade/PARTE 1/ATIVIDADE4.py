soma = 0
quantidade = 0
    
while True:
        num = float(input("Digite um número (ou 0 para sair): "))
        if num == 0:
            break
        soma += num
        quantidade += 1
        
print(f"Quantidade de números digitados: {quantidade} | Soma total: {soma}")