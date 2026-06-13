nome = input("Digite o nome do(a) aluno(a): ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media = (nota1 + nota2) / 2

print("\n=========================================")
print(f"Aluno(a): {nome}")
print(f"Média Final: {media:.1f}")
print("-----------------------------------------")

if media >= 6.0:
    print("Situação: APROVADO(A)")
else:
    print("Situação: EM RECUPERAÇÃO")

print("=========================================")
