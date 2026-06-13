matriz = []
soma_total = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        soma_total += valor  
    matriz.append(linha)

total_elementos = 9
media = soma_total / total_elementos

print("\nMatriz resultante:")
for linha in matriz:
    print(linha)

print(f"\nA média dos elementos da matriz é: {media:.2f}")
