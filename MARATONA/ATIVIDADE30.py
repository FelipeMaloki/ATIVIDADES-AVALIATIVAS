n = int(input("Digite um número: "))

if n < 0:
    print("Erro: Não existe fatorial de número negativo!")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print(f"O fatorial de {n} é: {fatorial}")
