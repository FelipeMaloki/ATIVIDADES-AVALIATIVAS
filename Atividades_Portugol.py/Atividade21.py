numero = int(input("Digite um número de 1 a 7 para saber o dia da semana: "))

if numero == 1:
    print("O dia correspondente é: Domingo")
elif numero == 2:
    print("O dia correspondente é: Segunda-feira")
elif numero == 3:
    print("O dia correspondente é: Terça-feira")
elif numero == 4:
    print("O dia correspondente é: Quarta-feira")
elif numero == 5:
    print("O dia correspondente é: Quinta-feira")
elif numero == 6:
    print("O dia correspondente é: Sexta-feira")
elif numero == 7:
    print("O dia correspondente é: Sábado")
else:
    print("Erro: O número digitado está fora do intervalo de 1 a 7!")
