matriz = []
soma_elementos = 0
diagonal_principal = []
    
    
for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
            soma_elementos += valor
            if i == j:
                diagonal_principal.append(valor)
        matriz.append(linha)
        
print("\nVisualização da Matriz 3x3:")
for linha in matriz:
        print(linha)
        
print(f"\nSoma de todos os elementos: {soma_elementos}")
print(f"Elementos da diagonal principal: {diagonal_principal}")