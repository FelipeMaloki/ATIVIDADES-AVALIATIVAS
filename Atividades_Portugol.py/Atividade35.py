print("=== ANÁLISE DE NOTAS - LÓGICA DE PROGRAMAÇÃO ===")

soma_notas = 0

for i in range(1, 26):
    nota = float(input(f"Digite a nota do {i}º aluno(a): "))
    soma_notas = soma_notas + nota
    
    if i == 1:
        maior_nota = nota
        menor_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

media_turma = soma_notas / 25

print("\n=========================================")
print("           RELATÓRIO DA TURMA            ")
print("=========================================")
print(f"Maior nota da turma: {maior_nota:.1f}")
print(f"Menor nota da turma: {menor_nota:.1f}")
print(f"Média geral da turma: {media_turma:.1f}")
print("=========================================")
