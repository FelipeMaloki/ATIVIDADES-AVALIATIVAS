nome = input("Digite o nome do(a) aluno(a): ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media = (nota1 + nota2) / 2

print("\n=========================================")
print(f"Aluno(a): {nome}")
print(f"Média Inicial: {media:.1f}")
print("-----------------------------------------")

if media >= 6.0:
    print("Situação: APROVADO(A)")
else:
    print("Situação: EM RECUPERAÇÃO")
    print("=========================================\n")
    
    
    nota_recuperacao = float(input("Digite a nota da prova de recuperação: "))
    
    print("\n=========================================")
    print(f"Nota da Recuperação: {nota_recuperacao:.1f}")
    print("-----------------------------------------")
    
    
    if nota_recuperacao >= 5.0:
        print("Situação Final: APROVADO(A) NA RECUPERAÇÃO")
    else:
        print("Situação Final: REPROVADO(A)")

print("=========================================")
