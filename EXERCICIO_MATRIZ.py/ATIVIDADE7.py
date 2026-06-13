matriz = []
soma_diagonal = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    soma_diagonal += matriz[i][i]

print("\nMatriz resultante:")
for linha in matriz:
    print(linha)

print(f"\nA soma dos elementos da diagonal principal é: {soma_diagonal}")
