matriz = []
maior_valor = None  

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
            
    matriz.append(linha)

print("\nMatriz resultante:")
for linha in matriz:
    print(linha)

print(f"\nO maior valor encontrado na matriz é: {maior_valor}")
