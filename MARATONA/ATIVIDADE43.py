def matrizes(matriz):
    linhas_originais = len(matriz)
    colunas_originais = len(matriz[0])
    
    matriz_vazia = []
    
    for c in range(colunas_originais):
        nova_linha = []
        
        for l in range(linhas_originais):
            nova_linha.append(matriz[l][c])
        matriz_vazia.append(nova_linha)
        
    return matriz_vazia

matriz = [[1, 2, 3], [4, 5, 6]]
print(matrizes(matriz))  