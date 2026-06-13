print("=== ACUMULADOR DE NÚMEROS: APENAS MAIORES QUE ZERO ===")
print("O programa encerrará quando a soma total chegar a 100.")
print("=====================================================")

soma = 0
quantidade = 0

while soma < 100:
    numero = 0
    while numero <= 0:
        numero = float(input("Digite un número maior que zero: "))
        if numero <= 0:
            print(" Entrada inválida! Digite apenas números maiores que 0.\n")

    soma = soma + numero
    quantidade = quantidade + 1
    
    print(f"-> Soma atual: {soma} | Números válidos digitados: {quantidade}\n")

print("=========================================")
print("           OBJETIVO ALCANÇADO            ")
print("=========================================")
print(f"Soma final alcançada: {soma}")
print(f"Quantidade de números válidos necessários: {quantidade}")
print("=========================================")
