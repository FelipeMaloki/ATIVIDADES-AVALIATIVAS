print("=== ACUMULADOR DE NÚMEROS ===")
print("O programa encerrará quando a soma total chegar a 100.")
print("=====================================================")

soma = 0
quantidade = 0

while soma < 100:
    numero = float(input("Digite um número: "))
    soma = soma + numero
    quantidade = quantidade + 1
    
    print(f"-> Soma atual: {soma} | Números digitados: {quantidade}\n")


print("=========================================")
print("           OBJETIVO ALCANÇADO            ")
print("=========================================")
print(f"Soma final alcançada: {soma}")
print(f"Quantidade de números necessários: {quantidade}")
print("=========================================")
