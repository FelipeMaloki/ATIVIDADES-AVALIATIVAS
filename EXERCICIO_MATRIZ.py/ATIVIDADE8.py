matriz = []
contador_pares = 0

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
        
        if valor % 2 == 0:
            contador_pares += 1
            
    matriz.append(linha)

print("\nMatriz preenchida:")
for linha in matriz:
    print(linha)

print(f"\nA matriz possui {contador_pares} números pares.")
