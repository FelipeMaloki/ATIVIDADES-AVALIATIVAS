def par(numero):
    return numero % 2 == 0

x = int(input("Digite um número: "))

if par(x):
    print(f"O número {x} é PAR.")
else:
    print(f"O número {x} é ÍMPAR.")
