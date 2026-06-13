print("=== SISTEMA DE BOLETIM BIMESTRAL ===")

nota_teste = float(input("Digite a nota do teste: "))
nota_prova = float(input("Digite a nota da prova: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))

media = (nota_teste + nota_prova) / 2

print("\n=========================================")
print("            RESULTADO FINAL              ")
print("=========================================")
print(f"Média do Aluno: {media:.1f}")
print(f"Total de Faltas: {faltas}")
print("-----------------------------------------")

if media < 5.0 or faltas >= 10:
    print("Situação: REPROVADO(A)")
    if faltas >= 10:
        print("Motivo: Excesso de faltas (limite máximo é 9).")

elif media >= 7.0 and faltas < 10:
    print("Situação: APROVADO(A)")

elif 5.0 <= media <= 6.9 and faltas < 10:
    print("Situação: EM RECUPERAÇÃO")

print("=========================================")
