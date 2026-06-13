print("A MÉDIA DO ALUNO")
soma = 0
for i in range(1, 6):
        num = float(input(f"Digite a {i}º nota do aluno: "))
        soma += num
        media = soma / 5
        print(f"Soma total: {soma} | Média dos números: {media}")