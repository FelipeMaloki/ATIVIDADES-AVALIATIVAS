# Inicialização da estrutura de armazenamento
boletim = []
num_alunos = 3
num_bimestres = 4
media_minima = 7.0

# Coleta de dados
for i in range(num_alunos):
    notas_aluno = []
    print(f"\n--- Digite as notas do Aluno {i + 1} ---")
    
    for j in range(num_bimestres):
        nota = float(input(f"Digite a nota do {j + 1}º Bimestre: "))
        notas_aluno.append(nota)
        
    boletim.append(notas_aluno)

print("\n" + "="*45)
print("   BOLETIM ESCOLAR  ")
print("="*45)


for i in range(num_alunos):
    notas = boletim[i]
    
    media = sum(notas) / num_bimestres
    
    if media >= media_minima:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    print(f"Aluno {i + 1}:")
    print(f"  > Notas: {notas}")
    print(f"  > Média Final: {media:.2f}")
    print(f"  > Situação: {situacao}")
    print("-" * 45)
