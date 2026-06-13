matriz = []
soma_total = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        soma_total += valor  
    matriz.append(linha)

print("\nMatriz resultante:")
for linha in matriz:
    print(linha)


print(f"\nA soma de todos os elementos é: {soma_total}")
