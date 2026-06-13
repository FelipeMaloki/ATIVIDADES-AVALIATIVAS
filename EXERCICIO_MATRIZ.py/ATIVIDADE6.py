matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz resultante:")
for linha in matriz:
    print(linha)

print("\n Os elementos da diagonal principal são:")

for i in range(3):
    print(matriz[i][i], end=" ")
print()  
